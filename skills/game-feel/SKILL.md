---
name: game-feel
description: Use when designing tactile satisfaction and juice for 2D game interactions, including quadratic trauma screen shake, hit-stop freeze frames, squash and stretch easing curves, impact particles, and micro-interaction feedback loops.
---

# Game Feel & Micro-Interaction Juice

## Overview
Defines the non-code mathematical and perceptual specifications that make a 2D one-finger action feel responsive, weighty, and satisfying across every touch, collision, and combo payoff.

## Core Juice Pillars

### 1. Input-to-Response Immediacy
- **Zero-Frame Input Acknowledgment:** Visual deformation (squash/stretch or aim line tension) must begin within `<16ms` (1 frame at 60Hz) of finger contact.
- **Input Forgiveness:** Specify hitbox padding (`+10% to +18%` on beneficial pickups, `-12%` on hazards) and grace windows (`80–120ms` coyote/buffer windows).

### 2. Quadratic Camera Trauma (`Shake = Trauma^2`)
- Accumulate normalized `trauma` $\in [0.0, 1.0]$ on impact events and decay linearly (`trauma_decay_per_sec`: `1.2 – 2.5`).
- Camera translational offset and rotational angle scale with $\text{Trauma}^2$ so minor bounces stay smooth while boss/core shatters deliver heavy impact without nauseating jitter.

### 3. Multi-Tier Hit-Stop (Real-Time Freeze Frames)
- **Tier 0 (High-Frequency Tick):** `0.0s` (`time_scale: 1.0`) — never freeze basic rapid bounces.
- **Tier 1 (Multiplier / Combo Split):** `0.015s – 0.025s` (`time_scale: 0.15`) — micro-punctuation.
- **Tier 2 (Obstacle Shatter):** `0.035s – 0.055s` (`time_scale: 0.05`) — tactile crunch weight.
- **Tier 3 (Core / Boss Detonation):** `0.075s – 0.110s` (`time_scale: 0.0`) — dramatic climax freeze before particle burst.

### 4. Squash & Stretch Conservation of Volume
- Impact scale vectors `[scaleX, scaleY]` must preserve perceived 2D area ($X \cdot Y \approx 1.0$, e.g., `[1.35, 0.72]`), restoring to `[1.0, 1.0]` over `0.09s – 0.14s` using `EaseOutBack` or `EaseOutElastic`.
