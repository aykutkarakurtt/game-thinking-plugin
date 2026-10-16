---
name: keep-kill-ideation
description: Use when brainstorming 2D hyper-casual or hybrid-casual game concepts, evaluating one-finger input mechanics, weighing CPI vs. retention trade-offs, or running Devil's Advocate Keep/Kill validation gates before locking a game concept.
---

# Keep/Kill Concept Ideation (2D Hyper-Casual)

## Overview
Structured ideation discipline that prevents clone concepts and premature documentation by forcing interactive question-driven framing, 2–3 distinct concept proposals, and a brutal Devil's Advocate (`Keep / Kill`) filter before locking a concept.

## When to Use
- Starting `/analyze` Stage 1 before generating any `outputs/game_thinking_report.md` or `outputs/game_balance.json` artifacts
- Evaluating whether a 2D one-finger mechanic has sufficient 3-second visual clarity and D1/D7 retention depth
- Filtering out high-CPI or over-scoped mechanics early

## Core Recipe (Stage 1 Gate)

1. **Anti-Repetition Check:** Inspect existing `outputs/game_thinking_report.md` and `outputs/game_balance.json` (if present). Never reuse a previously generated sub-genre or core mechanic.
2. **Focused Clarifying Question:** Ask one A/B/C/D multiple-choice question at a time to lock:
   - Target 2D sub-genre (e.g., Sorting/Puzzle, Timing/Physics, Runner/Multiplier, Stacking, Drawing, Slicing)
   - Primary player sensation & 3-second visual CPI hook
3. **2–3 Distinct 2D Concepts:** For each concept, specify strictly in this order:
   - **High Concept & 3-Second Visual CPI Hook**
   - **One-Finger Input Schema** (`Tap`, `Hold & Release`, `Drag/Sling`, `Swipe`)
   - **Trade-Off Matrix** (Pros, Cons, CPI Potential, Retention Risk)
4. **Devil's Advocate (`Keep / Kill` Verdict):** Explicitly state why weaker options must be **KILLED** (e.g., visual clutter in first 2 seconds, lack of clutch recovery, high production cost) and why the winning concept earns a **KEEP** verdict.
5. **Hard-Gate Approval:** Stop and wait for explicit user approval before entering Stage 2.

## Quick Reference: Keep vs. Kill Criteria

| Dimension | KEEP Signal | KILL Signal |
|---|---|---|
| **3-Second Readability** | Goal and failure state understood in `<1.5s` without UI text | Requires tutorial text or multi-step setup to understand |
| **Input Complexity** | Single thumb (`Tap`, `Drag`, `Hold & Release`) | Dual-stick, multi-button, or precision pinch gestures |
| **Depth-to-Scope Ratio** | Emergent physics/combo tension from 1 core rule | Needs 20+ handcrafted asset types to stay interesting |
| **Clutch Recovery** | Near-miss recovery feels skill-based and repeatable | Binary instant-death with zero recovery window |

## Red Flags — STOP and Re-Evaluate
- Proposing 3 variations of the same mechanic instead of 3 distinct concepts
- Skipping the user approval gate (`HARD-GATE`) and writing `game_balance.json` immediately
- Recommending a concept without naming its #1 churn risk and mitigation
