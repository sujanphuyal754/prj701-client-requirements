# Sprint 1 Retrospective

**Unit:** PRJ701 IT Capstone Project 1, KIHE, Trimester 2, 2026
**Sprint goal:** Deliver a verified decision matrix and defensible weight sets so Sprint 2 can rank and validate.

## Backlog and outcome

| ID | Item | Status |
|---|---|---|
| S1-1 | Literature search and case selection | Done |
| S1-2 | Case study investigation and gap analysis | Done |
| S1-3 | Criteria definitions and 0/1 scoring rule | Done |
| S1-4 | Verify all 60 matrix cells against the source | Done |
| S1-5 | AHP weights with consistency check (CR < 0.10) | Done |
| S1-6 | CRITIC weights | Done |
| S1-7 | Entropy weights with zero-information handling | Done |
| S1-8 | Combined weight set | Done |
| S1-9 | Client requirements document on GitHub | Done |
| S1-10 | Adviser review of the AHP judgements | Carried over to Sprint 2 |
| S1-11 (stretch) | Early ranking preview (TOPSIS, VIKOR, PROMETHEE-II) | Preview only; formal validation in Sprint 2 |

## What went well

- **Data quality check worked.** Checking every one of the 60 matrix cells against Table 5 caught one misread cell (Lucas [81], secure sharing) before any weights were calculated.
- **AHP judgements were consistent.** The consistency ratio was 0.011, well below the 0.10 limit, so the pairwise judgements are internally consistent.
- **Three weighting methods built and checked.** AHP, CRITIC and Entropy run in one formula-driven Excel workbook and matched an independent Python calculation with no differences.
- **Clear scope and a shared board.** The sprint backlog on Trello gave everyone the same definition of done, and 9 of 10 committed items were finished.
- **Requirements written down early.** The client requirements are on GitHub with priorities and acceptance criteria, so Sprint 2 can start from a clear list.

## What did not go so well

- **AHP judgements are assumed.** Table 5 contains only 0/1 data, so pairwise importance judgements cannot be derived from it. We set them ourselves and the planned adviser review did not happen in Sprint 1.
- **The weighting methods disagree strongly.** Entropy gives C3 40.5% and C2 only 3.0%, while AHP gives C4 42.6%. Averaging them was a team decision that still needs a written justification.
- **Ties and zero-information columns found late.** Five publications have identical profiles, and some columns carry little information. The handling rule was agreed after the first calculations, not before.
- **Documents drifted apart.** The schedule table in the proposal and its Excel version were first built with different layouts and had to be reconciled by hand.

## Feedback from the demo and Q&A

| Feedback received | Group response and action |
|---|---|
| _to be added after the session_ | |

## Improvement actions (for Sprint 2)

| Action | What will be done | When |
|---|---|---|
| Adviser review of the AHP judgements | Book a short review and record the outcome on the board. | Week 7 |
| Test each weight set on its own | In Sprint 2, run the rankings under AHP-only, CRITIC-only, Entropy-only and combined weights, and report how much the result changes. | Sprint 2 |
| Write the tie-handling rule first | Document the rule for ties and zero-information columns in the requirements before calculating. | Week 7 |
| One source of truth | Keep the data and schedule in one workbook that feeds the report and slides, so documents cannot drift apart. | Sprint 2 |
| Add verification to the definition of done | A card is only Done after a second member checks it against the source or an independent calculation. | Week 7 |
| Short weekly check-in | Hold a 10-minute check-in and move cards on the board, so blocked items such as the adviser review are seen early. | Weekly |
