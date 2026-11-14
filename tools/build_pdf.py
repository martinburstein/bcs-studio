"""Typeset reviewed laboratory Markdown. Layout only; no research parameters."""
from pathlib import Path
import argparse, hashlib, html, json, re, os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, KeepTogether
from reportlab.lib.utils import ImageReader
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def register_fonts():
    candidates=[Path(os.environ['CRYPTO_LAB_FONT_DIR'])] if os.environ.get('CRYPTO_LAB_FONT_DIR') else []
    candidates += [Path('/usr/share/fonts/truetype/dejavu'),Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype']
    font_dir=next((p for p in candidates if (p/'DejaVuSans.ttf').exists() and (p/'DejaVuSerif.ttf').exists()),None)
    if font_dir is None: raise SystemExit('Install DejaVu Sans/Serif or set CRYPTO_LAB_FONT_DIR to their directory.')
    for family in ('DejaVuSans', 'DejaVuSerif'):
        for suffix, style in (('', ''), ('-Bold', '-Bold'), ('-Italic' if family.endswith('Serif') else '-Oblique', '-Italic')):
            pdfmetrics.registerFont(TTFont(family+style, str(font_dir/(family+suffix+'.ttf'))))
        pdfmetrics.registerFontFamily(family,normal=family,bold=family+'-Bold',italic=family+'-Italic',boldItalic=family+'-Bold')

class LabDoc(SimpleDocTemplate):
    def beforeDocument(self):
        self.heading_count=0
        self.last_outline_level=-1
    def afterFlowable(self, flow):
        if isinstance(flow,Paragraph) and flow.style.name in ('Part','Chapter'):
            self.heading_count+=1
            key=f'chapter-{self.heading_count}'
            level=0 if flow.style.name=='Part' else 1
            if not hasattr(self,'last_outline_level'): self.last_outline_level=-1
            level=min(level,self.last_outline_level+1)
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flow.getPlainText(),key,level)
            show_toc=not (getattr(self,'omit_first_title_from_toc',False) and self.heading_count==1)
            if getattr(self,'toc_mode',None)=='black':
                text=flow.getPlainText()
                show_toc=(flow.style.name=='Part' and text.startswith(('Part ','Appendix.','Laboratory evidence'))) or bool(re.match(r'^[A-Z][A-Z0-9.]{1,7} - ',text))
            if show_toc:
                self.notify('TOCEntry',(level,flow.getPlainText(),self.page,key))
            self.last_outline_level=level

def formatted(text):
    # Render ASCII hyphens; preserve mathematical minus and original source bytes.
    text=text.replace('\u2014',' - ').translate({0x2010:45,0x2011:45,0x2012:45,0x2013:45})
    text=html.escape(text).replace('\n','<br/>')
    text=re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',r'<link href="\2" color="#24557A"><u>\1</u></link>',text)
    text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    text=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',text)
    text=re.sub(r'`([^`]+)`',r'<font name="DejaVuSans">\1</font>',text)
    return text

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('source',type=Path);ap.add_argument('output',type=Path)
    ap.add_argument('--kind',choices=['blue','paper','black'],required=True)
    ap.add_argument('--title',required=True);ap.add_argument('--subtitle',default='')
    ap.add_argument('--status',default='Research edition; not externally peer-reviewed')
    args=ap.parse_args()
    register_fonts()
    accent={'blue':'#164F88','paper':'#405B69','black':'#202727'}[args.kind]
    ink=colors.HexColor('#202C33');muted=colors.HexColor('#5C6972');ac=colors.HexColor(accent)
    body=ParagraphStyle('Body',fontName='DejaVuSerif',fontSize=10.4,leading=15.6,textColor=ink,spaceAfter=8)
    auxiliary_body=ParagraphStyle('Auxiliary body',parent=body,allowWidows=0,allowOrphans=0)
    reference=ParagraphStyle('Reference',parent=body,fontSize=9.2,leading=13.2,spaceAfter=6)
    small=ParagraphStyle('Small',parent=body,fontName='DejaVuSans',fontSize=8.1,leading=11.5,textColor=muted,spaceAfter=6)
    chapter=ParagraphStyle('Chapter',fontName='DejaVuSans-Bold',fontSize=16,leading=21,textColor=ac,spaceBefore=17,spaceAfter=11,keepWithNext=True)
    part=ParagraphStyle('Part',parent=chapter,fontSize=22,leading=28,spaceBefore=18,spaceAfter=15)
    sub=ParagraphStyle('Subhead',parent=chapter,fontSize=11.3,leading=15,spaceBefore=11,spaceAfter=7)
    quote=ParagraphStyle('Quote',parent=body,leftIndent=14,rightIndent=8,fontSize=10,leading=15,borderColor=colors.HexColor('#B7C8D4'),borderWidth=.6,borderPadding=8,backColor=colors.HexColor('#F3F6F8'),spaceBefore=5,spaceAfter=12)
    cell=ParagraphStyle('Cell',parent=small,textColor=ink,fontSize=8.1,leading=11)
    cover=ParagraphStyle('Cover',fontName='DejaVuSans-Bold',fontSize=30,leading=37,textColor=colors.white,spaceAfter=22)
    cover_small=ParagraphStyle('Cover small',fontName='DejaVuSans',fontSize=11,leading=17,textColor=colors.HexColor('#E1E8EC'),spaceAfter=14)
    para=lambda s,style=body:Paragraph(formatted(s),style)
    story=[Spacer(1,92),para(args.title,cover),para(args.subtitle,cover_small),Spacer(1,26),para('THE BIG CRYPTO SHORT',cover_small),para('Public research edition · 14 November 2026',cover_small),para(args.status,cover_small),PageBreak()]
    story.append(para('Contents',sub));toc=TableOfContents();toc.levelStyles=[ParagraphStyle('Contents part',parent=small,fontName='DejaVuSans-Bold',fontSize=10.3,leading=15.5,spaceBefore=8),ParagraphStyle('Contents chapter',parent=small,fontSize=9.4,leading=14,spaceBefore=4,leftIndent=12)];
    if args.kind=='black':
        toc.levelStyles=[ParagraphStyle('Black contents part',parent=small,fontName='DejaVuSans-Bold',fontSize=10,leading=12,spaceBefore=1,spaceAfter=0),ParagraphStyle('Black contents case',parent=small,fontSize=9.1,leading=10.6,spaceBefore=0,spaceAfter=0,leftIndent=12)]
        toc.tableStyle=TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)])
    story.extend([toc,PageBreak()])
    lines=args.source.read_text().splitlines();i=0;auxiliary_section=False
    while i<len(lines):
        raw_line=lines[i];line=raw_line.strip();i+=1
        if not line:continue
        if line=='<!-- pagebreak -->':story.append(PageBreak());continue
        if line.startswith('<!--'):continue
        if line.startswith('# '):
            auxiliary_section=args.kind=='black' and line.startswith('# Appendix.')
            story.append(para(line[2:],part));continue
        if line.startswith('## '):story.append(para(line[3:],chapter));continue
        if line.startswith('### '):story.append(para(line[4:],sub));continue
        match=re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)',line)
        if match:
            image_path=(args.source.parent/match[2]).resolve()
            width,height=ImageReader(str(image_path)).getSize();scale=min(504/width,560/height)
            story.extend([Image(str(image_path),width=width*scale,height=height*scale),para(match[1],small)])
            continue
        if line.startswith('|'):
            block=[line]
            while i<len(lines) and lines[i].strip().startswith('|'):block.append(lines[i].strip());i+=1
            rows=[[s.strip() for s in r.strip('|').split('|')] for r in block if not re.fullmatch(r'[\s|:\-]+',r)]
            n=len(rows[0]);rows=[r for r in rows if len(r)==n]
            widths=[504/n]*n
            if args.kind=='black' and n==3 and rows[0][0]=='ID' and rows[0][-1]=='URL':
                widths=[30,310,164]
            t=Table([[para(s,cell) for s in r] for r in rows],colWidths=widths,repeatRows=1,hAlign='LEFT')
            vertical_padding=5 if args.kind=='black' else 7
            t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E8EEF2')),('LINEBELOW',(0,0),(-1,0),.8,ac),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#CDD5DB')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),vertical_padding),('BOTTOMPADDING',(0,0),(-1,-1),vertical_padding)]))
            story.extend([t,Spacer(1,10)]);continue
        if line.startswith('```'):
            while i<len(lines) and not lines[i].strip().startswith('```'):story.append(para(lines[i],small));i+=1
            i+=1;continue
        if line.startswith('> '):story.append(para(line[2:],quote));continue
        if re.match(r'^[-*] ',line):story.append(para('• '+line[2:]));continue
        if re.match(r'^\d+\. ',line):story.append(para(line));continue
        block=[line];hard_break=raw_line.endswith('  ')
        while i<len(lines) and lines[i].strip() and not re.match(r'^(?:#|\||[-*] |\d+\. |```|<!--)',lines[i].strip()):
            next_raw=lines[i];block.append(('\n' if hard_break else ' ')+next_raw.strip());hard_break=next_raw.endswith('  ');i+=1
        paragraph_text=''.join(block)
        paragraph_style=reference if args.kind=='black' and (re.match(r'^\[(?:F|M)-[A-Z0-9]+\]',paragraph_text) or paragraph_text.startswith('**Primary sources and dates:**')) else (auxiliary_body if auxiliary_section else body)
        paragraph=para(paragraph_text,paragraph_style)
        story.append(KeepTogether([paragraph]) if paragraph_style is reference else paragraph)
    def page(canvas,doc):
        canvas.saveState()
        if doc.page==1:
            canvas.setFillColor(ac);canvas.rect(0,0,612,792,fill=1,stroke=0)
        else:
            canvas.setStrokeColor(ac);canvas.setLineWidth(.8);canvas.line(54,753,558,753)
            canvas.setFillColor(muted);canvas.setFont('DejaVuSans',7)
            canvas.drawString(54,764,'THE BIG CRYPTO SHORT  /  '+args.kind.upper())
            canvas.drawString(54,29,'Public edition · '+args.status)
            canvas.drawRightString(558,29,str(doc.page))
        canvas.restoreState()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    doc=LabDoc(str(args.output),pagesize=(612,792),leftMargin=54,rightMargin=54,topMargin=55,bottomMargin=54,title=args.title,author='The Big Crypto Short',pageCompression=1)
    doc.omit_first_title_from_toc=(args.kind=='paper')
    doc.toc_mode=args.kind
    doc.multiBuild(story,onFirstPage=page,onLaterPages=page)
    print(json.dumps({'source':str(args.source.resolve()),'sourceSha256':hashlib.sha256(args.source.read_bytes()).hexdigest(),'output':str(args.output.resolve()),'outputSha256':hashlib.sha256(args.output.read_bytes()).hexdigest(),'status':args.status}))

if __name__=='__main__':main()
