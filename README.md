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
| `workbook/MCDM_Complete_Analysis.xlsx` | Formula-driven workbook: AHP, CRITIC, Entropy, TOPSIS, VIKOR, PROMETHEE-II, sensitivity |
| `scripts/` | Independent Python calculation used to verify the workbook |

## Status

- Sprint 1 (weeks 1 to 6): FR1 to FR6 complete.
- Sprint 2 (weeks 7 to 10): FR7 to FR13 complete, FR14 (user guide and final report) in progress.

Retrospective board: see the Trello boards linked in the retrospective documents.

## Reproducing the results

```
pip install numpy scipy
python scripts/verify.py
```

## Reference

He, Y., Zhou, Z., Pan, Y., Chong, F., Wu, B., Xiao, K., & Li, H. (2024). Review of data security within energy blockchain: A comprehensive analysis of storage, management, and utilization. *High-Confidence Computing, 4*(3), Article 100233. https://doi.org/10.1016/j.hcc.2024.100233
