"""TOPSIS under each weighting (AHP, CRITIC, Entropy, Combined). Run: python scripts/topsis_all_weights.py"""
import csv, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute import all_results, promethee1, names, m
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(RES, exist_ok=True)
res = all_results()
SETS = ["AHP", "CRITIC", "Entropy", "Combined"]
print("Weights:"); [print(f"  {s:<9}" + "  ".join(f"C{k+1}={x:.3f}" for k, x in enumerate(res["sets"][s]))) for s in SETS]

rows = []
print("\nTOPSIS: closeness to the ideal solution (rank)")
print(f"{'Publication':<18}" + "".join(f"{s:>16}" for s in SETS))
for i in sorted(range(m), key=lambda i: res["topsis"]["Combined"]["rank"][i]):
    cells = [f"{res['topsis'][s]['C'][i]:.4f} ({res['topsis'][s]['rank'][i]})" for s in SETS]
    print(f"{names[i]:<18}" + "".join(f"{c:>16}" for c in cells))
    rows.append([names[i]] + [x for s in SETS for x in (round(float(res['topsis'][s]['C'][i]), 4), res['topsis'][s]['rank'][i])])
with open(os.path.join(RES, "topsis_all_weights.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["publication"] + [f"{s}_{k}" for s in SETS for k in ("closeness", "rank")]); w.writerows(rows)
print("\nSaved results/topsis_all_weights.csv")
