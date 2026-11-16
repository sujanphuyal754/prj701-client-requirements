"""VIKOR (v = 0.5) under each weighting (AHP, CRITIC, Entropy, Combined). Run: python scripts/vikor_all_weights.py"""
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
print("\nVIKOR: Q value (rank). Lower Q is better.")
print(f"{'Publication':<18}" + "".join(f"{s:>16}" for s in SETS))
for i in sorted(range(m), key=lambda i: res["vikor"]["Combined"]["rank"][i]):
    cells = [f"{res['vikor'][s]['Q'][i]:.4f} ({res['vikor'][s]['rank'][i]})" for s in SETS]
    print(f"{names[i]:<18}" + "".join(f"{c:>16}" for c in cells))
    rows.append([names[i]] + [x for s in SETS for x in (round(float(res['vikor'][s]['S'][i]), 4), round(float(res['vikor'][s]['R'][i]), 4), round(float(res['vikor'][s]['Q'][i]), 4), res['vikor'][s]['rank'][i])])
print("\nVIKOR acceptance conditions for the best alternative:")
for s in SETS:
    v = res["vikor"][s]
    print(f"  {s:<9} best = {names[v['a1']]:<16} Q gap {v['gap']:.3f} vs threshold {v['DQ']:.3f}  C1 (advantage) = {v['c1']}  C2 (stability) = {v['c2']}")
with open(os.path.join(RES, "vikor_all_weights.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["publication"] + [f"{s}_{k}" for s in SETS for k in ("S", "R", "Q", "rank")]); w.writerows(rows)
print("\nSaved results/vikor_all_weights.csv")
