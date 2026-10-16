---
name: physics-tuning
description: Use when specifying 2D physics simulation parameters, fixed timestep rates, continuous collision detection (CCD), velocity caps, restitution/bounciness, drag, gravity scale, or anti-sticking deflection angles in game_balance.json.
---

# 2D Physics Tuning & Simulation Balance

## Overview
Provides engine-neutral mathematical rules for tuning stable, deterministic-feeling 2D physics parameters inside `game_balance.json` without tunneling, infinite-loop sticking, or frame-rate jitter.

## Core Mathematical Rules

### 1. Fixed Timestep & Render Interpolation
- Always specify `fixed_timestep_sec: 0.01666` (`physics_hz: 60`) or `0.00833` (`120 Hz` for ultra-fast slicing/pinball) with `render_interpolation: true`.

### 2. Anti-Tunneling Guardrails (CCD + Speed Cap)
- Fast 2D projectiles skip across thin colliders when $\text{Speed} / \text{PhysicsHz} > \text{ColliderThickness}$.
- Always pair `continuous_collision_detection: true` with an explicit `max_speed_cap_units_per_sec` (`35.0 – 50.0` units/sec) and minimum collider radius (`>= 0.20` units).

### 3. Restitution, Drag & Anti-Sticking Deflection
| Parameter | Recommended 2D Range | Design Purpose |
|---|---|---|
| `gravity_scale` | `0.0` (top-down/ricochet) or `1.8 – 3.2` (platform/drop) | Snappier falls than default 1.0 earth gravity |
| `linear_drag` | `0.0` (elastic bounce) or `0.5 – 4.0` (swipe/slide) | Controls deceleration crispness after finger release |
| `restitution_bounciness` | `0.0` (stacking) to `1.0` (pure ricochet) | Energy retention per collision |
| `min_bounce_angle_deflection_deg` | `3.5° – 6.0°` | Prevents infinite horizontal wall-to-wall softlocks |
