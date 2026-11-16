"""The 12 combinations: 4 ranking methods x 3 weightings.

Methods   : TOPSIS, VIKOR (v = 0.5), PROMETHEE I (partial ranking), PROMETHEE II (complete ranking)
Weightings: AHP, CRITIC, Entropy
Run from the repository root:   python scripts/run_12_combinations.py

PROMETHEE I gives a partial ranking, so it has no single rank per publication. Here it is shown as a
level: level 1 holds every publication that no other publication outranks, level 2 holds those that
are outranked only by level 1, and so on. Publications on the same level are not ordered by PROMETHEE I.
"""
import csv, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute import all_results, promethee1, names, m

RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(RES, exist_ok=True)
res = all_results()
WEIGHTINGS = ["AHP", "CRITIC", "Entropy"]
METHODS = ["TOPSIS", "VIKOR", "PROMETHEE I", "PROMETHEE II"]

def levels(M):
    """Level of each publication in the PROMETHEE I partial ranking."""
    left, lvl, k = set(range(m)), [0] * m, 1
    while left:
        top = [i for i in left if not any(M[j][i] == ">" for j in left if j != i)]
        for i in top: lvl[i] = k
        left -= set(top); k += 1
    return lvl

table = {}   # (method, weighting) -> list of 12 values (rank or level)
for w in WEIGHTINGS:
    table[("TOPSIS", w)] = res["topsis"][w]["rank"]
    table[("VIKOR", w)] = res["vikor"][w]["rank"]
    table[("PROMETHEE I", w)] = levels(promethee1(res["sets"][w])["M"])
    table[("PROMETHEE II", w)] = res["prom"][w]["rank"]

print("Weights:")
for w in WEIGHTINGS: print(f"  {w:<8}" + "  ".join(f"C{k+1}={x:.3f}" for k, x in enumerate(res["sets"][w])))
print("\nRank per publication (PROMETHEE I shows its level; equal numbers = tied or not separated)\n")
for w in WEIGHTINGS:
    print(f"--- {w} weights ---")
    print(f"{'Publication':<18}" + "".join(f"{x:>14}" for x in METHODS))
    for i in sorted(range(m), key=lambda i: (table[("PROMETHEE II", w)][i], names[i])):
        print(f"{names[i]:<18}" + "".join(f"{table[(x, w)][i]:>14}" for x in METHODS))
    print()
print("Best publication in each of the 12 combinations:")
for w in WEIGHTINGS:
    for x in METHODS:
        best = [names[i] for i in range(m) if table[(x, w)][i] == 1]
        print(f"  {x:<13} + {w:<8} -> {', '.join(best)}")

with open(os.path.join(RES, "12_combinations.csv"), "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["publication"] + [f"{x} + {w}" for w in WEIGHTINGS for x in METHODS])
    for i in range(m):
        wr.writerow([names[i]] + [table[(x, w)][i] for w in WEIGHTINGS for x in METHODS])
print("\nSaved results/12_combinations.csv")
