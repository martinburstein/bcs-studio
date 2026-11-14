"""Independent finite replay of P3-P6; no cryptographic/attack code."""
from fractions import Fraction
from itertools import product
from json import dump
from pathlib import Path
from argparse import ArgumentParser


def payoff(x, b, c, arch):
    good = all(x) if arch == 'B' else any(x)
    return tuple(b[i] * int(good) - c[i] * x[i] for i in range(len(x)))


def nes(b, c, arch):
    out = set()
    for x in product((0, 1), repeat=len(b)):
        u = payoff(x, b, c, arch)
        if all(payoff(x[:i] + (1-x[i],) + x[i+1:], b, c, arch)[i] <= u[i]
               for i in range(len(b))):
            out.add(x)
    return out


states_even = ((0,0,0),(1,1,0),(1,0,1),(0,1,1))
parity_marg = [Fraction(sum(s[i] for s in states_even), 4) for i in range(3)]
parity_pair = [Fraction(sum(s[i] and s[j] for s in states_even), 4)
               for i,j in ((0,1),(0,2),(1,2))]
assert parity_marg == [Fraction(1,2)]*3
assert parity_pair == [Fraction(1,4)]*3
assert not all((1,1,1) in states_even for _ in (0,))

case_count = profile_count = welfare_count = transfer_count = 0
for n in (2,3):
    for b in product(range(4), repeat=n):
        for c in product(range(1,4), repeat=n):
            case_count += 1
            profs = list(product((0,1), repeat=n))
            profile_count += 2*len(profs)
            ub = nes(b,c,'B')
            expected_b = {(0,)*n} | ({(1,)*n} if all(bi >= ci for bi,ci in zip(b,c)) else set())
            assert ub == expected_b
            we = [sum(payoff(x,b,c,'B')) for x in profs]
            assert max(we) == max(0, sum(b)-sum(c))
            assert all(sum(payoff(x,b,c,'B')) < 0 for x in profs if any(x) and not all(x))
            ue = nes(b,c,'E')
            expected_e = set()
            if all(bi <= ci for bi,ci in zip(b,c)):
                expected_e.add((0,)*n)
            for i,(bi,ci) in enumerate(zip(b,c)):
                if bi >= ci:
                    x=[0]*n; x[i]=1; expected_e.add(tuple(x))
            assert ue == expected_e
            we = [sum(payoff(x,b,c,'E')) for x in profs]
            assert max(we) == max(0, sum(b)-min(c))
            welfare_count += 2
            S = sum(bi-ci for bi,ci in zip(b,c))
            if S >= 0:
                t = tuple(Fraction(ci-bi,1)+Fraction(S,n) for bi,ci in zip(b,c))
                assert sum(t) == 0
                assert all(Fraction(bi-ci,1)+ti == Fraction(S,n) >= 0 for bi,ci,ti in zip(b,c,t))
                transfer_count += 1

mixed = ((3,5,1,2),(5,7,2,3),(4,9,1,4),(8,11,3,5))
for b1,b2,c1,c2 in mixed:
    assert b1>c1>0 and b2>c2>0
    p1,p2=Fraction(c2,b2),Fraction(c1,b1)
    assert b1*p2-c1 == 0 and b2*p1-c2 == 0
    q1,q2=1-p1,1-p2
    assert b1-c1 == b1*q2 and b2-c2 == b2*q1

assert case_count == 1872 and profile_count == 28800 and welfare_count == 3744 and transfer_count == 649
out = {
  'status':'passed',
  'method':'Independent checker written for this review; exact integer and Fraction arithmetic; exhaustive profiles and unilateral deviations on the specified finite grid.',
  'p3':{'evenParityMarginals':['1/2']*3,'evenParityPairwiseIntersections':['1/4']*3,'evenParityTriple':'0','independentTriple':'1/8'},
  'p4ComplementaryCases':case_count,'p5SharedProviderCases':case_count,
  'welfareChecks':welfare_count,'transferFeasibilityCases':transfer_count,
  'actionProfilesAcrossBothGames':profile_count,'p6MixedExamples':len(mixed),
  'domain':{'n':[2,3],'benefits':'integer 0..3','costs':'integer 1..3'},
  'limits':['Finite-grid replay confirms stated formulas only on the enumerated domain; general proofs remain algebraic under explicit assumptions.','No empirical, deployment, AI-capability, attack, loss, or portfolio inference.']
}
parser=ArgumentParser(description=__doc__)
parser.add_argument('--output', required=True, help='Path for results; choose a writable destination outside frozen source artifacts')
args=parser.parse_args()
output=Path(args.output)
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(__import__('json').dumps(out,indent=2)+'\n')
print(__import__('json').dumps(out,indent=2))
