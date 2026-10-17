---
description: Interactive Brainstorm-First game thinking workflow — clarify direction via questions, evaluate concepts with Keep/Kill trade-offs, then generate market intelligence, competitor deconstruction, MDA/Juice matrix, README.md, and game_balance.json.
agent: game-designer
---

You are executing the **Brainstorm-First Game Design, Market & Thinking Workflow**.

Target input / focus: `$ARGUMENTS`

Strictly follow this two-stage **Thinking Lead** methodology (NO GDD bloat, NO production code, NO visual asset generation):

---

## STAGE 1: Interactive Brainstorming & Concept Lock (`HARD-GATE`)
Before generating full analysis documents or touching `README.md` / `game_balance.json`, you MUST first run an interactive brainstorming session with the user:

### Step 1.1: Invoke Brainstorming & Clarifying Questions
- Invoke the `brainstorming` and `keep-kill-ideation` skills.
- Inspect existing `README.md` and `game_balance.json` (if present) to ensure you NEVER repeat previously generated sub-genres or mechanics.
- Ask **one focused question at a time** (prefer multiple-choice options A/B/C/D plus an autonomous option) to clarify:
  1. Target 2D hyper-casual / hybrid-casual sub-genre or core mechanic direction (incorporating `$ARGUMENTS` if provided).
  2. Primary player sensation / 3-second visual CPI hook preference.

### Step 1.2: Propose 2-3 Novel Concepts + Devil's Advocate (`Keep / Kill` Test)
- Based on the user's answers, present **2-3 distinct, non-clone 2D concepts** in chat:
  * **High Concept & 3-Second Visual CPI Hook**
  * **One-Finger Core Mechanic & Input Schema**
  * **Trade-Off Analysis** (Pros, Cons, CPI Potential, Retention Risk)
  * **Devil's Advocate (`Keep / Kill` Verdict)**: Brutally test why weaker options should be killed or pivoted, and why the recommended concept survives.
- **STOP and ask for explicit user approval (`HARD-GATE`)** on which concept to lock in before proceeding to Stage 2.

---

## STAGE 2: Deep Thinking, Deconstruction & Mathematical Balance (Post-Approval)
Once the user explicitly approves the chosen concept in Stage 1, execute all phases below tailored 100% to the approved concept:

### Phase 1: Autonomous Market & CPI Hook Intelligence (`market-cpi-deconstruction`)
- Analyze why the chosen mechanic resonates in current mobile charts and viral social channels (TikTok / Meta).
- Break down the exact **3-Second Visual Hook** choreography (0-1s tension, 1-2s input/twist, 2-3s satisfying payoff).

### Phase 2: Competitor Deconstruction (`market-cpi-deconstruction`)
- Benchmark **2-3 top market leaders** in the chosen sub-genre.
- Deconstruct:
  1. **Core Psychological & Mechanical Driver**: Why did their primary loop click?
  2. **Friction Points & Churn Risks**: Where does player satisfaction drop?
  3. **Untapped Market Gap**: How our brainstormed concept exploits this gap.

### Phase 3: 2D MDA & Juice Matrix Choreography (`mda-juice-choreography`)
- **Mechanics**: Input schema, physics rules, fail/win states.
- **Dynamics**: Tension-release pacing, risk/reward loops, clutch recovery moments.
- **Aesthetics**: Tactile ASMR satisfaction and visual clarity.
- **Juice Blueprint**: Quantified micro-interactions — quadratic trauma screen shake, multi-tier hit-stop (ms), squash & stretch easing curves, particle burst emission counts, and audio frequency layering (`Hz`).

### Phase 4: Mathematical Game Balance (`mathematical-game-balance`)
- Engineer a complete, production-ready mathematical parameter set in `game_balance.json` tailored to the approved concept using the exact root sections required by `GameBalanceConfig` in `validate_balance.py`:
  - `meta` (`oyun_adi`/`game_title`, `surum`, `tur`/`sub_genre`, `tasarim_lideri`, `denge_modeli`, `tarih`)
  - `<concept>_mechanics` (Player input, speed, responsiveness, hitbox parameters)
  - `physics_and_collision_tuning` (`simulation` + concept collision rules)
  - `difficulty_progression_curves` (`formulas` dict + `level_milestones` list)
  - `juice_and_game_feel_matrix` (`screen_shake_trauma`, `hit_stop_freeze_frames`, `squash_and_stretch`, `particle_choreography`)
  - `scoring_and_combo_economy` (`combo_multiplier_step`, `max_combo_multiplier`, etc.)

### Phase 5: Deliverable Artifact Generation & Pydantic Schema Validation
1. Write the strategic Thinking, Market Deconstruction, MDA/Juice, and Keep/Kill report to `README.md` (strictly Thinking Lead scope — do NOT turn it into a bloated production GDD).
2. Write the standalone, mathematically validated configuration to `game_balance.json` conforming to the Pydantic v2 `GameBalanceConfig` schema in `validate_balance.py`.
3. Run `python3 validate_balance.py` to verify that `game_balance.json` passes all Pydantic v2 `BaseModel` type and range constraints.
4. Present a concise executive summary in the CLI output.

**Remember:** Do NOT write C# code or generate art assets. Strictly operate within Game Thinking, Market Strategy, Competitor Deconstruction, Game Feel, and Mathematical Balance.
