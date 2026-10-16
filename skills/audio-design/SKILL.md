---
name: audio-design
description: Use when designing the audio mixing architecture, bus hierarchy, target loudness (LUFS), sidechain ducking in decibels, or harmonic ASMR pitch escalation rules inside the 2D Juice Matrix and game_balance.json.
---

# Game Audio Architecture & ASMR Pitch Choreography

## Overview
Defines the quantitative audio mixing, bus routing, sidechain ducking (`dB`), and combo-driven harmonic pitch escalation (`Hz`) specifications for 2D hyper-casual and hybrid-casual games.

## Core Audio Balance Specifications

### 1. Bus Hierarchy & Loudness Target
- Standard 2D mixer tree: `["Master", "Music", "SFX_Impacts", "SFX_ASMR", "UI"]`.
- Normalize master target loudness to `master_target_loudness_lufs: -14.0` (`-16.0 to -12.0 LUFS` range) to prevent mobile speaker clipping during multi-object cascades.

### 2. Sidechain Ducking (Clarity Under Impacts)
- Route high-priority satisfaction cues (`SFX_Glass`, `SFX_Shatter`, or `SFX_Combo`) as the `trigger_bus` to duck `Music`:
  - `duck_gain_db`: `-6.0 to -10.0 dB` (must be negative)
  - `attack_ms`: `10 – 25 ms` (instant transient clearance)
  - `release_ms`: `250 – 450 ms` (smooth musical recovery without pumping)

### 3. Harmonic Combo Pitch Escalation (ASMR Dopamine)
- Rapid consecutive hits/sorts/bounces must never play at a flat, robotic pitch:
  - Specify `base_freq_hz` (e.g., `520 – 720 Hz` for crisp tactile pings) and `max_freq_hz` (`2000 – 2600 Hz` ceiling).
  - Escalate pitch by `pitch_step_per_combo`: `+0.03 to +0.06` semitone/ratio per chained event within `pitch_reset_idle_window_sec` (`0.50 – 0.85s`).
  - Anchor heavy destruction payoffs with a low sub-bass layer (`55 – 75 Hz`).
