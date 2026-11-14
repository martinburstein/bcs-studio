# Exact finite-model checks

Run from the repository root with Python 3.9+; both scripts use only the standard library:

```sh
python3 reproducibility/replay.py --output /absolute/writable/path/replay.json
python3 reproducibility/independent-replay.py --output /absolute/writable/path/independent.json
```

Both scripts are preserved from the internally reviewed working-paper edition. They enumerate the specified finite integer grid with exact integer/Fraction arithmetic: 1,872 cases per architecture, 3,744 welfare checks, 649 transfer-feasibility cases, 28,800 candidate action profiles and four mixed-indifference examples. These are finite-domain consistency checks, not general proofs or external independent replications.

The stored results in this directory were reproduced for this public package. No cryptographic attack, deployed system, AI capability, empirical probability, market quote, personal portfolio or trading instrument is tested.

PDFs were built from the Markdown with `tools/build_pdf.py`, using ReportLab and DejaVu fonts. See that script's `--help` for the three document kinds. The PDF visual-review record is in `publication/qa.json`.
