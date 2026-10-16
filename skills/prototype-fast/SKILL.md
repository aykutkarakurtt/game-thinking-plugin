---
name: prototype-fast
description: Use when scoping a 2D game mechanic for rapid MVP validation, defining observable Keep/Kill criteria, or stripping non-essential features to test whether the core one-finger verb is fun within 30 seconds.
---

# Prototype Fast (MVP Scope & Keep/Kill Criteria)

## Overview
Evaluates a 2D game mechanic by isolating its single core verb, stripping away meta-bloat, and defining observable **Keep / Kill / Refactor** criteria before committing to production GDD or engine implementation.

## Core Principles for Thinking Lead

1. **State the One Question:** Define the single mechanical hypothesis the concept must prove (e.g., *"Does triggering a mid-air shockwave during a multi-ball ricochet create a satisfying skill ceiling?"*).
2. **Isolate the Core Verb:** Strip out stores, skins, narrative, and complex menus. A hyper-casual concept lives or dies on the 3-second repetition of its primary one-finger action.
3. **Observable Keep / Kill Signals:**

| Verdict | Observable Design Criteria |
|---|---|
| **KEEP** | • Uncoached player understands the core verb within `<3 seconds` from visual motion alone.<br>• Core action produces immediate tactile curiosity ("one more try" compulsion).<br>• Difficulty scales mathematically via 2–3 parameters (speed, density,HP) without needing 50 unique asset types. |
| **KILL** | • Mechanic requires text tutorials or complex UI indicators to understand.<br>• Core loop has long passive waiting windows where player input is locked out.<br>• Fun depends on heavy content production rather than physics/timing dynamics. |
| **REFACTOR** | • Core verb is compelling, but a single timing window or punish state feels unfair — retune hitbox forgiveness or cooldowns in `game_balance.json`. |
