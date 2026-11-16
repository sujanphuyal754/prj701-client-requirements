# Sprint 2 Retrospective

**Unit:** PRJ701 IT Capstone Project 1, KIHE, Trimester 2, 2026
**Sprint goal:** Rank the publications with TOPSIS, VIKOR, PROMETHEE I and PROMETHEE II, check agreement and test stability.

## Backlog and outcome

| ID | Item | Status |
|---|---|---|
| S2-1 | TOPSIS ranking with combined weights (FR7) | Done |
| S2-2 | VIKOR ranking, v = 0.5, with acceptance conditions (FR8) | Done |
| S2-3 | PROMETHEE I (partial) and PROMETHEE-II (complete) rankings, linear preference function (FR9) | Done |
| S2-4 | Equal ranks for ties and mean rank across methods (FR10) | Done |
| S2-5 | Sensitivity analysis and critical criterion (FR11) | Done |
| S2-6 | Agreement between methods, Spearman correlation (FR12) | Done |
| S2-7 | Rankings under AHP-only, CRITIC-only, Entropy-only weights | Done |
| S2-8 | Editable Excel workbook with live formulas (FR13) | Done |
| S2-9 | User guide and final report draft (FR14) | In progress |
| S2-10 | Adviser review of the AHP judgements | Not completed |

## What went well

- **Tie rule written before calculating.** The rule from the Sprint 1 retrospective was applied: tied alternatives get equal ranks, so the five identical publications all share rank 4 instead of being ordered by chance.
- **Excel matched the independent check.** The formula-driven workbook and an independent Python calculation gave the same weights and rankings for all three methods.
- **PROMETHEE I shows where the evidence conflicts.** Li et al. [42], Bai et al. [48] and Yang et al. [77] are not outranked by any publication, but none of them outranks another, so the order inside the top three depends on the method used.
- **VIKOR and PROMETHEE-II agree closely.** Their rankings have a Spearman correlation of 0.977, and VIKOR's acceptance conditions were met for Li et al. [42].
- **Sensitivity analysis found the weak point.** Reducing the C1 weight by only 2.9% changes a rank order, so C1 is the most critical criterion, followed by C5 (3.0%). Knowing this lets us state how far the result can be trusted.

## What did not go so well

- **TOPSIS disagrees with the other two methods.** TOPSIS correlates with VIKOR at only 0.52 and with PROMETHEE-II at 0.49. Wu et al. [20] is ranked 4th by TOPSIS but 11th by the others, and we do not yet have a firm explanation.
- **The ranking is fragile to small weight changes.** A 2.9% reduction in the C1 weight is enough to change a rank order, which is small given that the weights themselves come from three methods that disagree.
- **Binary data leaves many ties.** Five publications are identical, so no method can separate them. Only the top three and the bottom of the ranking are clearly distinct.
- **AHP judgements still not reviewed.** The adviser review carried over from Sprint 1 was not completed, so the AHP judgements remain our own assumption and must be stated as a limitation.

## Feedback from the demo and Q&A

| Feedback received | Group response and action |
|---|---|
| _to be added after the session_ | |

## Improvement actions (for the final phase)

| Action | What will be done | When |
|---|---|---|
| Report rankings as tiers | In the final report present the top three, the middle group and the bottom as tiers, and state that exact positions inside a tie are not meaningful. | Week 11 |
| Explain the TOPSIS difference | Show, for Wu et al. [20] and Wang et al. [78], which criteria drive TOPSIS differently from VIKOR and PROMETHEE-II, and write it up. | Week 11 |
| Book the adviser review | Fix a date for the AHP review in week 11 and record the outcome, or state the limitation clearly if it cannot happen. | Week 11 |
| Finish and test the user guide | Complete the guide and ask someone outside the group to follow it on the workbook, then fix what they find unclear. | Week 11 |
| Final consistency check | Before submission, check that the report, workbook, slides, Trello and GitHub all show the same numbers, with a second member checking each. | Week 12 |
| Freeze the results on GitHub | Tag the final workbook and requirements in the repository so the submitted version cannot change. | Week 12 |
