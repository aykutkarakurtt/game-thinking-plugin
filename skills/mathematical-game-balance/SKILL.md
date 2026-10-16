---
name: mathematical-game-balance
description: Use when modeling 2D game physics parameters, designing difficulty progression formulas (exponential, logarithmic, linear), balancing scoring and combo economies, or generating and validating game_balance.json against the Pydantic v2 schema.
---

# Mathematical Game Balance & Pydantic Validation

## Overview
Engineers production-ready mathematical balance configurations (`outputs/game_balance.json`) for 2D hyper-casual and hybrid-casual games and validates them against the studio's Pydantic v2 Data Contract (`schemas/game_balance_schema.py`).

## When to Use
- Executing `/analyze` Stage 2 (Phases 4 and 5)
- Designing level progression formulas, 2D physics simulation constants, and combo economy curves
- Validating `game_balance.json` before handoff to the GDD or Engine stage

## Core Balance Architecture

### 1. Required Root Blocks (`GameBalanceConfig`)
Every generated `game_balance.json` must contain these 5 mandatory Pydantic-validated blocks plus at least 1 concept-specific mechanics block:
1. `meta`: `oyun_adi`, `surum`, `tur`, `tasarim_lideri`, `denge_modeli`, `tarih` (`YYYY-MM-DD`), `aciklama`
2. `<concept>_mechanics`: Concept-specific input, speed, cooldown, and hitbox parameters
3. `physics_and_collision_tuning`: Must include `simulation` (`fixed_timestep_sec: 0.01666`, `physics_hz: 60`, `continuous_collision_detection`, `render_interpolation`, `gravity_scale`, `linear_drag`, `restitution_bounciness`, `friction`)
4. `difficulty_progression_curves`:
   - `formulas`: At least 2 explicit mathematical functions (e.g., `HP(lvl) = floor(a * pow(lvl, b) + c * lvl)`, logarithmic caps `min(cap, base + floor(ln(lvl + 1) * k))`)
   - `level_milestones`: At least 3 ascending level snapshots (`level: 1, 5, 12, 25...`) with concrete evaluated numbers
5. `juice_and_game_feel_matrix` & `scoring_and_combo_economy`

### 2. Progression Curve Selection Guide

| Curve Type | Formula Pattern | Best Used For |
|---|---|---|
| **Sub-Linear / Polynomial** | $f(L) = a \cdot L^{1.25} + b \cdot L$ | Obstacle HP, target score requirements |
| **Logarithmic Cap** | $f(L) = \min(M, b + \lfloor k \cdot \ln(L + 1) \rfloor)$ | Hazard spawn density, speed multipliers, gate caps |
| **Stepwise Decay** | $f(L) = \max(m, B - \lfloor L / s \rfloor)$ | Allowed moves/shots, combo grace windows |

## Mandatory Verification Step
After writing `game_balance.json`, always execute:
```bash
python3 validate_balance.py
```
If Pydantic raises a `ValidationError`, fix the offending field types or out-of-range numbers immediately before completing `/analyze`.
