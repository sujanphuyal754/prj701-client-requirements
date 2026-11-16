"""Run every ranking method under every weight set.

Methods : TOPSIS, VIKOR (v = 0.5), PROMETHEE I (partial), PROMETHEE II (complete)
Weights : Combined, AHP, CRITIC, Entropy
Output  : a table for each weight set on screen, and ../results/rankings_all_weight_sets.csv

Run from the repository root:   python scripts/run_all_rankings.py
"""
import csv, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute import all_results, promethee1, rk, names, crit, m

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "rankings_all_weight_sets.csv")

res = all_results()
rows = []
for wname, w in res["sets"].items():
    top, vik, pro = res["topsis"][wname]["rank"], res["vikor"][wname]["rank"], res["prom"][wname]["rank"]
    p1 = promethee1(w)
    mean = np.mean([top, vik, pro], axis=0)
    final = rk(mean, desc=False)                      # equal ranks for ties, lowest mean rank first
    print("\n" + "=" * 92)
    print(f"Weight set: {wname}   weights " + "  ".join(f"C{k+1}={x:.3f}" for k, x in enumerate(w)))
    print(f"{'Publication':<18}{'TOPSIS':>8}{'VIKOR':>8}{'PROM-II':>9}{'Mean':>7}{'Final':>7}   PROMETHEE I (outranks / outranked by / incomparable)")
    for i in sorted(range(m), key=lambda i: (final[i], names[i])):
        M = p1["M"][i]
        o, b, inc = M.count(">"), M.count("<"), M.count("?")
        print(f"{names[i]:<18}{top[i]:>8}{vik[i]:>8}{pro[i]:>9}{mean[i]:>7.2f}{final[i]:>7}   {o} / {b} / {inc}")
        rows.append([wname, names[i], top[i], vik[i], pro[i], o, b, inc, round(float(mean[i]), 2), final[i]])
    c = p1["cnt"]
    print(f"PROMETHEE I pairs: {c['>']} outranked, {c['=']} indifferent, {c['?']} incomparable (of {m*(m-1)//2})")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["weight_set", "publication", "topsis_rank", "vikor_rank", "promethee_ii_rank",
                 "promethee_i_outranks", "promethee_i_outranked_by", "promethee_i_incomparable", "mean_rank", "final_rank"])
    wr.writerows(rows)
print(f"\nSaved {len(rows)} rows to results/rankings_all_weight_sets.csv")
