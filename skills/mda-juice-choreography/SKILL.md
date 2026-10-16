---
name: mda-juice-choreography
description: Use when deconstructing 2D game mechanics into MDA (Mechanics, Dynamics, Aesthetics) or specifying quantified game feel and juice parameters including quadratic trauma screen shake, multi-tier hit-stop freeze frames, squash and stretch curves, particle bursts, and ASMR audio frequencies.
---

# 2D MDA & Quantified Juice Choreography

## Overview
Translates abstract "good game feel" into a mathematically quantified 2D MDA (Mechanics, Dynamics, Aesthetics) and Micro-Interaction Juice Matrix ready for GDD and engine implementation.

## When to Use
- Executing `/analyze` Stage 2 (Phase 3)
- Designing tactile feedback for single-finger 2D actions (`Input -> Immediate Juice -> State Change -> Reward -> Progression`)
- Populating `juice_and_game_feel_matrix` inside `game_balance.json`

## 1. 2D MDA Framework Breakdown
- **Mechanics (Rules & Input):** Exact touch input vector, hitbox forgiveness (coyote time / padding), physics state transitions, and win/fail conditions.
- **Dynamics (Emergent Pacing):** Tension-release oscillation, risk/reward decisions, and clutch recovery windows.
- **Aesthetics (Player Sensation):** Primary emotional target (e.g., Kinetic Destruction, ASMR Order, Precision Flow, Escalating Frenzy).

## 2. Quantified Juice Matrix Standards

| Juice Layer | Mathematical Model / Parameter Standard | Typical 2D Range |
|---|---|---|
| **Screen Shake (Trauma)** | Quadratic trauma model: $\text{Shake} = \text{Trauma}^2$, linear decay per sec | `trauma_decay_per_sec`: `1.2 – 2.5`<br>`event_trauma`: `0.02 – 0.85` |
| **Hit-Stop (Freeze Frames)** | Multi-tier real-time pause (`duration_realtime_sec` + `time_scale`) | Tier 0 (Minor): `0ms`<br>Tier 1 (Medium): `15–25ms`<br>Tier 2 (Heavy): `35–55ms`<br>Tier 3 (Boss/Clear): `70–110ms` |
| **Squash & Stretch** | Non-uniform scale deformation `[scaleX, scaleY]` conserving area ($X \cdot Y \approx 1$) | Impact: `[1.35, 0.72]`<br>Restore: `0.08–0.15s` (`EaseOutBack`) |
| **Particle Choreography** | Burst count, angular spread (`deg`), initial speed range, lifetime (`sec`) | Minor: `6–10` particles (`0.2s`)<br>Shatter: `18–30` particles (`0.5s`) |
| **Audio & ASMR Mixing** | Bus hierarchy, target loudness (`-14 LUFS`), sidechain ducking (`dB`), harmonic pitch step | Ducking: `-6.0 to -10.0 dB`<br>Pitch step: `+0.03 to +0.06` per combo |

## Common Mistakes
- **Hit-Stop on Every Minor Tick:** Freezing the screen on rapid basic bounces/taps ruins flow; reserve `Tier 0 (0.0s)` for high-frequency events and `Tier 1–3` for milestone impacts.
- **Linear Screen Shake:** Using `Shake = Trauma` instead of `Shake = Trauma^2` makes small hits feel jittery and large hits feel flat.
