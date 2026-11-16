# Client Requirements: Energy Blockchain Data-Sharing Decision Framework

**Unit:** PRJ701 IT Capstone Project 1, KIHE, Trimester 2, 2026
**Document status:** Sprint 2 version (FR1 to FR13 complete, FR14 in progress)
**Maintained by:** Sujan Phuyal and group members

## 1. Project summary

Energy-blockchain architects must choose among published data-sharing solutions, but the evidence available is a qualitative comparison table (He et al., 2024, Table 5). This project delivers a validated, reusable decision framework that ranks twelve solutions against five problems and shows how stable the ranking is.

## 2. Client and stakeholders

| Stakeholder | Interest |
|---|---|
| Client: energy-sector architects and blockchain developers | A transparent way to shortlist data-sharing solutions and justify the choice |
| Unit coordinator and academic adviser | A project that meets the unit requirements and is academically sound |
| Project group | A feasible scope delivered in 12 project weeks |

## 3. Scope

**In scope:** the 12 × 5 decision matrix from Table 5; AHP, CRITIC and Entropy weighting; TOPSIS, VIKOR and PROMETHEE-II ranking; sensitivity analysis; an Excel workbook, user guide and final report.

**Out of scope:** building a blockchain system, collecting new primary data, and extending the study to other case studies (future work).

## 4. User stories

- As an energy-blockchain architect, I want the solutions ranked against agreed criteria, so that I can shortlist them with evidence.
- As an architect, I want to change the importance of a criterion and see the ranking update, so that I can test my own priorities.
- As a reviewer, I want to see every formula and source reference, so that I can check the results.
- As a reviewer, I want to know how much the ranking changes when weights change, so that I know how far to trust it.

## 5. Functional requirements

Priority uses MoSCoW (Must, Should).

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR1 | Hold the 12 × 5 binary decision matrix from He et al. (2024), Table 5, with source references | Must | Done (Sprint 1) |
| FR2 | Define the five criteria and the 0/1 scoring rule (all benefit criteria) | Must | Done (Sprint 1) |
| FR3 | Calculate AHP weights and a consistency ratio, accepted only if below 0.10 | Must | Done (Sprint 1) |
| FR4 | Calculate CRITIC weights from standard deviation and correlation | Must | Done (Sprint 1) |
| FR5 | Calculate Entropy weights and handle zero-information columns | Must | Done (Sprint 1) |
| FR6 | Combine the three weight sets into one combined set | Must | Done (Sprint 1) |
| FR7 | Rank alternatives with TOPSIS | Must | Done (Sprint 2) |
| FR8 | Rank alternatives with VIKOR (v = 0.5) and report its acceptance conditions | Must | Done (Sprint 2) |
| FR9 | Rank alternatives with PROMETHEE I (partial ranking from the leaving and entering flows) and PROMETHEE-II (complete ranking from the net flow), using a linear preference function | Must | Done (Sprint 2) |
| FR10 | Give tied alternatives equal ranks and report a mean rank across methods | Must | Done (Sprint 2) |
| FR11 | Run sensitivity analysis and identify the most critical criterion | Must | Done (Sprint 2) |
| FR12 | Measure agreement between methods (Spearman rank correlation) | Should | Done (Sprint 2) |
| FR13 | Let the user edit judgements and weights and see results update | Should | Done (Sprint 2) |
| FR14 | Provide a short user guide and a final report | Should | In progress (Sprint 2) |

## 6. Non-functional requirements

| ID | Quality | Requirement |
|---|---|---|
| NFR1 | Accuracy | Excel results match an independent Python calculation to four decimal places |
| NFR2 | Transparency | All calculations are visible formulas, not hidden values |
| NFR3 | Usability | The tool can be used without programming skills |
| NFR4 | Reproducibility | Another group can repeat the analysis from the repository |
| NFR5 | Maintainability | Files are version controlled on GitHub with a change log |
| NFR6 | Security and integrity | Formula cells are protected from accidental change, and repository access follows least privilege (added in the design phase, Week 11) |
| NFR7 | Performance | The workbook recalculates in under five seconds on a standard laptop (added in the design phase, Week 11) |

## 7. Data requirements

- Source: He et al. (2024), Table 5, twelve publications scored 1 (addresses the problem) or 0 (does not) on five criteria: C1 Multi-domain collaboration, C2 Efficiency overhead, C3 Poor traceability, C4 Secure sharing, C5 Legitimate fairness.
- All five criteria are benefit criteria.
- All 60 cells were checked against the source in Sprint 1. One misread cell was found and corrected.

## 8. Assumptions and constraints

- The AHP pairwise judgements are the group's own, because Table 5 contains only 0/1 data. The adviser review was not completed in Sprint 2, so they remain an assumption and are reported as a limitation.
- The combined weights are the simple average of the AHP, CRITIC and Entropy weights.
- Tied alternatives receive equal (standard competition) ranks.
- The project uses published data only, so no ethics approval is needed beyond expert review of the judgements.
- Delivery is within 12 project weeks using Excel and Python.
- Results are reported as tiers, because five alternatives are identical and the ranking changes with a weight change of under 3% in C1.

## 9. Acceptance criteria

1. The workbook matches the independent Python calculation to four decimal places (NFR1).
2. The AHP consistency ratio is below 0.10 (FR3). **Sprint 1 result: 0.011.**
3. Rankings are produced by TOPSIS, VIKOR, PROMETHEE I and PROMETHEE-II under four weight sets.
4. The sensitivity analysis names the most critical criterion and a re-run with the changed weight confirms it. **Sprint 2 result: C1, at a 2.9% weight reduction; C5 is next at 3.0%.**
5. A user can edit weights and see updated results without programming (FR13). **Met in Sprint 2.**

## 10. Sprint 1 results (for traceability)

| Weight set | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|
| Combined | 18.5% | 12.6% | 27.2% | 23.8% | 18.0% |
| AHP | 9.7% | 15.9% | 25.9% | 42.6% | 5.9% |
| CRITIC | 23.2% | 18.9% | 15.1% | 24.0% | 18.8% |
| Entropy | 22.6% | 3.0% | 40.5% | 4.7% | 29.2% |

## 10a. Sprint 2 results (for traceability)

| Publication | TOPSIS | VIKOR | PROMETHEE-II | Mean rank | Final rank |
|---|---|---|---|---|---|
| Li et al. [42] | 1 | 1 | 3 | 1.67 | 1 |
| Bai et al. [48] | 3 | 2 | 1 | 2.00 | 2 |
| Yang et al. [77] | 2 | 3 | 2 | 2.33 | 3 |
| He et al. [80] | 7 | 4 | 4 | 5.00 | 4 |
| Hao et al. [82] | 7 | 4 | 4 | 5.00 | 4 |
| Shang et al. [83] | 7 | 4 | 4 | 5.00 | 4 |
| Zhang et al. [84] | 7 | 4 | 4 | 5.00 | 4 |
| Zhang [85] | 7 | 4 | 4 | 5.00 | 4 |
| Wang et al. [79] | 5 | 9 | 9 | 7.67 | 9 |
| Lucas et al. [81] | 5 | 9 | 9 | 7.67 | 9 |
| Wu et al. [20] | 4 | 11 | 11 | 8.67 | 11 |
| Wang et al. [78] | 12 | 12 | 12 | 12.00 | 12 |

PROMETHEE I (combined weights, 66 pairs): 27 pairs have one publication outranking the other, 11 are indifferent (the five identical publications) and 28 are incomparable. Li et al. [42], Bai et al. [48] and Yang et al. [77] are not outranked by any publication, but none of them outranks another, so PROMETHEE I does not order the top three; PROMETHEE-II orders them Bai, Yang, Li by net flow.

Spearman correlation between methods: VIKOR and PROMETHEE-II 0.977; TOPSIS and VIKOR 0.517; TOPSIS and PROMETHEE-II 0.494.

Smallest weight change that alters a rank order: C1 2.9%, C2 26.9%, C3 12.5%, C4 22.1%, C5 3.0%.

## 11. Suggested repository structure

```
/docs        client_requirements.md, retrospectives, user guide
/data        table5_decision_matrix.csv
/workbook    MCDM_Complete_Analysis.xlsx
/scripts     python verification scripts
README.md
```

## 12. Change log

| Date | Change | By |
|---|---|---|
| Sprint 1 | First version; FR1 to FR6 completed | Group |
| Sprint 2 | FR7 to FR13 completed; FR14 in progress; results and limitations added | Group |
| Design phase | NFR6 (security and integrity) and NFR7 (performance) added; see the Systems Design Document | Group |

## Reference

He, Y., Zhou, Z., Pan, Y., Chong, F., Wu, B., Xiao, K., & Li, H. (2024). Review of data security within energy blockchain: A comprehensive analysis of storage, management, and utilization. *High-Confidence Computing, 4*(3), Article 100233. https://doi.org/10.1016/j.hcc.2024.100233
