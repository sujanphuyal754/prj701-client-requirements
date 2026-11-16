# Energy Blockchain Data-Sharing Decision Framework

PRJ701 IT Capstone Project 1, Kingsford Institute of Higher Education (KIHE), Trimester 2, 2026.

A hybrid multi-criteria decision framework that ranks twelve published data-sharing solutions for energy blockchain against five problems, using the case study in He et al. (2024), Table 5.

## Contents

| Path | What it holds |
|---|---|
| `docs/Client_Requirements.md` | Client requirements: 14 functional and 5 non-functional requirements, scope, user stories, assumptions, acceptance criteria, results and change log |
| `docs/retrospective_sprint1.md` | Sprint 1 retrospective (what went well, what did not, improvements) |
| `docs/retrospective_sprint2.md` | Sprint 2 retrospective |
| `data/table5_decision_matrix.csv` | The 12 × 5 binary decision matrix |
| `workbook/MCDM_Complete_Analysis.xlsx` | Formula-driven workbook: AHP, CRITIC, Entropy, TOPSIS, VIKOR, PROMETHEE I and II, sensitivity |
| `scripts/` | Independent Python calculation used to verify the workbook; `mcdm_12_combinations.py` is the same 12-combination run as one standalone file; `run_12_combinations.py` runs the 12 combinations (TOPSIS, VIKOR, PROMETHEE I and PROMETHEE II, each with AHP, CRITIC and Entropy); `topsis_all_weights.py`, `vikor_all_weights.py` and `promethee_all_weights.py` show one method under AHP, CRITIC, Entropy and Combined weights |
| `results/` | Output of the scripts above, as `.csv` and readable `.txt` files |

## Status

- Sprint 1 (weeks 1 to 6): FR1 to FR6 complete.
- Sprint 2 (weeks 7 to 10): FR7 to FR13 complete, FR14 (user guide and final report) in progress.

Retrospective board: see the Trello boards linked in the retrospective documents.

## Reproducing the results

```
pip install numpy scipy
cd scripts && python verify.py
cd .. && python scripts/run_12_combinations.py     # the 12 combinations: 4 methods x AHP, CRITIC, Entropy
python scripts/topsis_all_weights.py      # TOPSIS with AHP, CRITIC, Entropy, Combined
python scripts/vikor_all_weights.py       # VIKOR with each weighting
python scripts/promethee_all_weights.py   # PROMETHEE I and II with each weighting
```

## Reference

He, Y., Zhou, Z., Pan, Y., Chong, F., Wu, B., Xiao, K., & Li, H. (2024). Review of data security within energy blockchain: A comprehensive analysis of storage, management, and utilization. *High-Confidence Computing, 4*(3), Article 100233. https://doi.org/10.1016/j.hcc.2024.100233
