# 🎯 `game-thinking-plugin` — Autonomous Game Design, Market & Thinking Lead Plugin

> **OpenCode Studio Plugin for 2D Hyper-Casual & Hybrid-Casual Games**  
> **Role:** Strategic Game Thinking, Interactive Brainstorming, Keep/Kill Validation, Market & Competitor Deconstruction, 2D MDA/Juice Choreography, and Mathematical Balance (`game_balance.json`).

---

## 🧭 Studio Role & Strict Boundaries

In a modular AI Game Studio pipeline, **`game-thinking-plugin`** acts as the **Pre-Production Thinking & Mathematical Balance Brain**:

* ❌ **NO Production Code:** Never writes C#, GDScript, shaders, or engine scripts.
* ❌ **NO Visual Assets:** Never generates sprites, textures, or UI art.
* ❌ **NO Bloated Production GDD:** Leaves level-by-level tables and store wireframes to the GDD/Production agent.
* ✅ **100% Thinking, Market & Balance Scope:** Turns raw ideas into validated concepts and exports production-ready mathematical parameters (`game_balance.json`) for downstream studio agents.

---

## 📚 Reference Methodologies

1. **Obra Superpowers (`obra/superpowers`):**
   * **Brainstorm-First Discipline:** Clarifies intent through focused, one-at-a-time questions before generating artifacts.
   * **Trade-Off & Devil's Advocate (`Keep / Kill`) Gate:** Evaluates 2–3 distinct concepts against CPI, retention, and scope risks, waiting for explicit human approval (`HARD-GATE`).
2. **Claude Code Game Studios (`Game Designer / Thinking Discipline`):**
   * **2D MDA Deconstruction:** Mechanics (Input/Physics) $\to$ Dynamics (Risk/Reward & Pacing) $\to$ Aesthetics (Tactile ASMR & Visual Clarity).
   * **Quantified Juice Matrix (`game-feel` & `audio-design`):** Quadratic trauma screen shake ($\text{Shake} = \text{Trauma}^2$), multi-tier real-time hit-stop (`ms`), squash & stretch tween curves, and harmonic audio pitch escalation (`Hz` / `dB`).
   * **Mathematical Balance (`physics-tuning` & `procedural-gen`):** Outputs engine-ready formulas and constants into `game_balance.json`.

---

## 📦 Installation & Usage

### Option A: Load as a Plugin in Another OpenCode Project (Studio Pipeline)
Add the plugin to your studio project's `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": [
    "github:aykutkarakurtt/game-thinking-plugin"
  ]
}
```

### Option B: Clone & Run Directly
```bash
git clone https://github.com/aykutkarakurtt/game-thinking-plugin.git
cd game-thinking-plugin
opencode
```

---

## ⚡ Custom Command: `/analyze` (Brainstorm-First Pipeline)

Run `/analyze` (or `/analyze <sub-genre/mechanic>`) in OpenCode to trigger the two-stage workflow:

```text
[ /analyze ]
     │
     ├──► STAGE 1: Interactive Brainstorming & Keep/Kill Gate (HARD-GATE)
     │      ├─ Step 1.1: Focused clarifying question (A/B/C/D sub-genre & CPI hook)
     │      ├─ Step 1.2: 2-3 Novel 2D Concepts + Trade-Offs + Devil's Advocate (Keep/Kill)
     │      └─ Step 1.3: Wait for explicit user approval before generating files
     │
     └──► STAGE 2: Deep Thinking, Deconstruction & Mathematical Balance
            ├─ Phase 1: 3-Second Visual CPI Hook & Market Resonance
            ├─ Phase 2: Competitor Deconstruction (2-3 leaders, churn risks, market gap)
            ├─ Phase 3: 2D MDA & Quantified Juice Matrix (Trauma, Hit-Stop, Audio Hz)
            └─ Phase 4: Output Generation (`game_balance.json` + Strategic Report)
```

---

## 🗂 Repository Structure

```text
game-thinking-plugin/
├── .opencode/
│   ├── agents/
│   │   └── game-designer.md      # Primary Thinking Lead agent definition
│   ├── commands/
│   │   └── analyze.md            # /analyze Brainstorm-First custom command
│   └── plugins/
│       └── game-designer.js      # OpenCode plugin entry point (auto-registers agent, command & rules)
├── AGENTS.md                     # Core methodological rules & anti-repetition constraints
├── opencode.json                 # Local OpenCode configuration
├── package.json                  # Plugin package manifest
└── README.md                     # Plugin documentation
```

---

## 📄 Output Artifact Schema (`game_balance.json`)

When `/analyze` completes Stage 2, it generates a standalone `game_balance.json` file for downstream studio agents (GDD / Developer):

```json
{
  "meta": {
    "oyun_adi": "Ricochet Pulse: Neon Shatter",
    "tur": "2D Hiper-Gündelik / Kinetik Sapan, Çarpan Kapıları ve Zincirleme Sekme Yıkımı"
  },
  "player_sling_and_pulse_mechanics": { "...": "Input & core verb parameters" },
  "physics_and_collision_tuning": { "...": "Fixed timestep, CCD, restitution, gates" },
  "difficulty_progression_curves": {
    "formulas": {
      "block_hp_formula": "BlockHP(lvl) = floor(12 * pow(lvl, 1.32) + 8 * lvl)"
    }
  },
  "juice_and_game_feel_matrix": {
    "screen_shake_trauma": { "model": "Shake = Trauma^2", "trauma_decay_per_sec": 1.65 },
    "hit_stop_freeze_frames": { "...": "Multi-tier real-time freeze durations (ms)" },
    "squash_and_stretch": { "...": "EaseOutBack scale vectors" },
    "audio_design_and_mixing": { "...": "Bus hierarchy, sidechain ducking (dB), pitch Hz" }
  },
  "scoring_and_combo_economy": { "...": "Combo windows & multipliers" }
}
```
