#!/usr/bin/env python3
"""Finite exact checks for propositions about two stylized migration games.

This script uses only the Python standard library. It contains no cryptographic
attack code and makes no inference about deployment, probability, or markets.
"""
from argparse import ArgumentParser
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def payoff(profile, benefits, costs, architecture):
    protected = int(all(profile)) if architecture == "B" else int(any(profile))
    return tuple(benefits[i] * protected - costs[i] * profile[i]
                 for i in range(len(profile)))


def equilibria(benefits, costs, architecture):
    found = set()
    for profile in product((0, 1), repeat=len(benefits)):
        current = payoff(profile, benefits, costs, architecture)
        stable = True
        for i in range(len(profile)):
            deviation = profile[:i] + (1 - profile[i],) + profile[i + 1:]
            if payoff(deviation, benefits, costs, architecture)[i] > current[i]:
                stable = False
                break
        if stable:
            found.add(profile)
    return found


def verify_case(benefits, costs):
    n = len(benefits)
    profiles = list(product((0, 1), repeat=n))
    b_expected = {(0,) * n}
    if all(b >= c for b, c in zip(benefits, costs)):
        b_expected.add((1,) * n)
    assert equilibria(benefits, costs, "B") == b_expected
    b_welfare = [sum(payoff(x, benefits, costs, "B")) for x in profiles]
    assert max(b_welfare) == max(0, sum(benefits) - sum(costs))
    assert all(sum(payoff(x, benefits, costs, "B")) < 0
               for x in profiles if any(x) and not all(x))

    e_expected = set()
    if all(b <= c for b, c in zip(benefits, costs)):
        e_expected.add((0,) * n)
    for i, (b, c) in enumerate(zip(benefits, costs)):
        if b >= c:
            x = [0] * n
            x[i] = 1
            e_expected.add(tuple(x))
    assert equilibria(benefits, costs, "E") == e_expected
    e_welfare = [sum(payoff(x, benefits, costs, "E")) for x in profiles]
    assert max(e_welfare) == max(0, sum(benefits) - min(costs))

    surplus = sum(b - c for b, c in zip(benefits, costs))
    transfer_checked = 0
    if surplus >= 0:
        transfers = tuple(Fraction(c - b, 1) + Fraction(surplus, n)
                          for b, c in zip(benefits, costs))
        assert sum(transfers) == 0
        assert all(Fraction(b - c, 1) + t == Fraction(surplus, n)
                   for b, c, t in zip(benefits, costs, transfers))
        assert all(Fraction(b - c, 1) + t >= 0
                   for b, c, t in zip(benefits, costs, transfers))
        transfer_checked = 1
    return transfer_checked, 2 * len(profiles)


def verify_p3():
    even_parity = {state: Fraction(1, 4)
                   for state in ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1))}
    independent = {state: Fraction(1, 8) for state in product((0, 1), repeat=3)}

    def moments(distribution):
        marginals = [sum(w for s, w in distribution.items() if s[i]) for i in range(3)]
        pairs = [sum(w for s, w in distribution.items() if s[i] and s[j])
                 for i, j in ((0, 1), (0, 2), (1, 2))]
        triple = sum(w for s, w in distribution.items() if all(s))
        return marginals, pairs, triple

    a, b = moments(even_parity), moments(independent)
    assert a[0] == b[0] == [Fraction(1, 2)] * 3
    assert a[1] == b[1] == [Fraction(1, 4)] * 3
    assert a[2] == 0 and b[2] == Fraction(1, 8)
    return a, b


def verify_p6():
    examples = ((3, 5, 1, 2), (5, 7, 2, 3), (4, 9, 1, 4), (8, 11, 3, 5))
    checked = 0
    for b1, b2, c1, c2 in examples:
        assert b1 > c1 > 0 and b2 > c2 > 0
        p_b = (Fraction(c2, b2), Fraction(c1, b1))
        p_e = (1 - Fraction(c2, b2), 1 - Fraction(c1, b1))
        assert all(0 < p < 1 for p in p_b + p_e)
        assert b1 * p_b[1] - c1 == 0 and b2 * p_b[0] - c2 == 0
        assert b1 - c1 == b1 * p_e[1] and b2 - c2 == b2 * p_e[0]
        checked += 1
    return checked


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True,
                        help="Path for exact JSON results; use a writable non-frozen output path")
    args = parser.parse_args()

    b_cases = e_cases = welfare_cases = transfer_cases = action_profiles = 0
    for n in (2, 3):
        for benefits in product(range(4), repeat=n):
            for costs in product(range(1, 4), repeat=n):
                transfers, profiles = verify_case(benefits, costs)
                b_cases += 1
                e_cases += 1
                welfare_cases += 2
                transfer_cases += transfers
                action_profiles += profiles
    p3a, p3b = verify_p3()
    p6 = verify_p6()
    result = {
        "status": "passed",
        "method": "Exhaustive action-profile and unilateral-deviation enumeration with exact integer/Fraction arithmetic.",
        "p3": {
            "marginals": [str(x) for x in p3a[0]],
            "pairIntersections": [str(x) for x in p3a[1]],
            "tripleIntersectionEvenParity": str(p3a[2]),
            "tripleIntersectionIndependent": str(p3b[2])
        },
        "p4ComplementaryGameCases": b_cases,
        "p5SharedProviderGameCases": e_cases,
        "welfareFormulaCases": welfare_cases,
        "p4TransferFeasibilityCases": transfer_cases,
        "actionProfilesVisitedAcrossBothArchitectures": action_profiles,
        "p6MixedIndifferenceExamples": p6,
        "domain": {"actors": [2, 3], "benefitsPerActor": "integer 0..3", "costsPerActor": "integer 1..3"},
        "limitations": [
            "Finite integer parameter grids only; no proof for all real values or arbitrary n.",
            "P4/P5 pure-equilibrium and welfare checks are limited to the enumerated grids.",
            "P6 checks four interior mixed-indifference examples, not a general equilibrium characterization.",
            "No attack code, AI capability, deployment, adaptation, empirical probability, loss or portfolio inference."
        ]
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
