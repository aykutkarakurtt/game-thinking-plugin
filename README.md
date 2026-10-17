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
│   │   └── game-designer.md                  # Primary Thinking Lead agent definition
│   ├── commands/
│   │   └── analyze.md                        # /analyze Brainstorm-First custom command
│   └── plugins/
│       └── game-designer.js                  # OpenCode plugin entry point (registers agent, command, skills & rules)
├── skills/                                   # 9 Modular Domain Skills (SKILL.md)
│   ├── brainstorming/
│   │   └── SKILL.md                          # Interactive Questioning, Trade-Offs & Approval Gate (HARD-GATE)
│   ├── prototype-fast/
│   │   └── SKILL.md                          # Rapid MVP Scoping & Observable Keep/Kill Criteria
│   ├── keep-kill-ideation/
│   │   └── SKILL.md                          # Stage 1 Ideation, Trade-Offs & Devil's Advocate Keep/Kill Gate
│   ├── market-cpi-deconstruction/
│   │   └── SKILL.md                          # 3-Second CPI Hook Choreography & Competitor Deconstruction
│   ├── mda-juice-choreography/
│   │   └── SKILL.md                          # 2D MDA Deconstruction & Micro-Interaction Choreography
│   ├── game-feel/
│   │   └── SKILL.md                          # Quadratic Trauma Shake, Hit-Stop Tiers & Squash/Stretch
│   ├── audio-design/
│   │   └── SKILL.md                          # Bus Hierarchy, -14 LUFS, Sidechain Ducking & ASMR Pitch Hz
│   ├── physics-tuning/
│   │   └── SKILL.md                          # 60Hz Fixed Timestep, CCD, Speed Caps & Bounce Deflection
│   └── mathematical-game-balance/
│       └── SKILL.md                          # Progression Curves, Scoring Economy & Pydantic Balance Modeling
├── validate_balance.py                       # All-in-one Pydantic v2 BaseModel schemas & CLI validator for game_balance.json
├── requirements.txt                          # Python dependency (pydantic>=2.0.0)
├── AGENTS.md                                 # Core methodological rules & anti-repetition constraints
├── opencode.json                             # Local OpenCode configuration
├── package.json                              # Plugin package manifest
└── README.md                                 # Plugin documentation
```

---

## 🧠 Bundled Domain Skills (`skills/`)

The plugin packages **9 specialized Game Thinking skills** directly inside `skills/` that `game-designer` loads on demand during `/analyze`:

| Skill Name | Purpose & Trigger |
|---|---|
| **`brainstorming`** | Interactive one-at-a-time questioning, trade-off framing, and explicit approval gate (`HARD-GATE`). |
| **`prototype-fast`** | Core verb isolation, MVP scope discipline, and observable Keep / Kill / Refactor signals. |
| **`keep-kill-ideation`** | One-finger 2D concept ideation, CPI vs. retention trade-off matrix, and Devil's Advocate (`Keep / Kill`) validation gate. |
| **`market-cpi-deconstruction`** | 3-second TikTok/Meta CPI hook choreography (`0-1s`, `1-2s`, `2-3s`) and 2–3 competitor churn/gap deconstruction. |
| **`mda-juice-choreography`** | 2D MDA (Mechanics, Dynamics, Aesthetics) deconstruction and micro-interaction juice matrix. |
| **`game-feel`** | Quadratic trauma screen shake ($\text{Shake} = \text{Trauma}^2$), multi-tier hit-stop (`ms`), squash & stretch, and input forgiveness. |
| **`audio-design`** | Audio mixer bus hierarchy, `-14 LUFS` loudness target, sidechain ducking (`dB`), and harmonic ASMR pitch escalation (`Hz`). |
| **`physics-tuning`** | 60Hz fixed timestep, continuous collision detection (CCD), velocity caps, and anti-sticking bounce deflection. |
| **`mathematical-game-balance`** | Polynomial/logarithmic progression formulas, scoring economy, and Pydantic v2 `game_balance.json` generation. |

---

## 🛡 Pydantic v2 Schema Validation (`validate_balance.py`)

To ensure a 100% type-safe handoff from the **Thinking Stage** to downstream **GDD** and **Engine/Developer** agents, all generated `game_balance.json` files are validated against a strict **Pydantic v2 (`BaseModel`)** schema defined in `validate_balance.py`:

* **Validated Models:** `GameBalanceConfig`, `MetaConfig`, `CpiHookSummary`, `CompetitorBenchmark`, `KeepKillVerdict`, `MdaSummary`, `PhysicsSimulationConfig`, `DifficultyProgressionCurves`, `ScreenShakeTraumaConfig`, `HitStopTierConfig`, `AudioDesignAndMixingConfig`, `ScoringAndComboEconomy`.
* **Mathematical Guardrails:** Enforces physics tick bounds (`30–240 Hz`), normalized trauma increments (`0.0–1.0`), ascending level milestones, negative sidechain ducking gain (`dB`), and real-time hit-stop limits (`0–500 ms`).

### Run Validation
```bash
pip install -r requirements.txt
python3 validate_balance.py
```

