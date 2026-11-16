"""PROMETHEE I (partial) and PROMETHEE II (complete) under each weighting. Run: python scripts/promethee_all_weights.py"""
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
print("\nPROMETHEE II: net flow (rank)")
print(f"{'Publication':<18}" + "".join(f"{s:>16}" for s in SETS))
order = sorted(range(m), key=lambda i: res["prom"]["Combined"]["rank"][i])
for i in order:
    cells = [f"{res['prom'][s]['phi'][i]:+.4f} ({res['prom'][s]['rank'][i]})" for s in SETS]
    print(f"{names[i]:<18}" + "".join(f"{c:>16}" for c in cells))
print("\nPROMETHEE I: outranks / outranked by / incomparable (out of 11 other publications)")
print(f"{'Publication':<18}" + "".join(f"{s:>16}" for s in SETS))
P1 = {s: promethee1(res["sets"][s]) for s in SETS}
for i in order:
    cells = [f"{P1[s]['M'][i].count('>')} / {P1[s]['M'][i].count('<')} / {P1[s]['M'][i].count('?')}" for s in SETS]
    print(f"{names[i]:<18}" + "".join(f"{c:>16}" for c in cells))
    rows.append([names[i]] + [x for s in SETS for x in (round(float(res['prom'][s]['pp'][i]), 4), round(float(res['prom'][s]['pm'][i]), 4), round(float(res['prom'][s]['phi'][i]), 4), res['prom'][s]['rank'][i], P1[s]['M'][i].count('>'), P1[s]['M'][i].count('<'), P1[s]['M'][i].count('?'))])
print("\nPROMETHEE I pairs (of 66):")
for s in SETS: c = P1[s]["cnt"]; print(f"  {s:<9} {c['>']} outranked, {c['=']} indifferent, {c['?']} incomparable")
with open(os.path.join(RES, "promethee_all_weights.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["publication"] + [f"{s}_{k}" for s in SETS for k in ("phi_plus", "phi_minus", "phi_net", "rank_II", "I_outranks", "I_outranked_by", "I_incomparable")]); w.writerows(rows)
print("\nSaved results/promethee_all_weights.csv")
