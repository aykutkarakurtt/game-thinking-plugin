#!/usr/bin/env python3
"""
Pydantic v2 Data Contract, Schema Models & CLI Validator for `game_balance.json`.

Used in the Unico AI Game Studio pipeline to guarantee that the output of the
Thinking & Balance stage (`game-thinking-plugin`) is strictly typed,
mathematically bounded, and safe for downstream consumption by the GDD and
Engine/Developer agents.

Usage:
    python3 validate_balance.py [path_to_game_balance.json]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional
from pydantic import (
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)


# ============================================================================
# 1. PYDANTIC V2 DATA CONTRACT MODELS (`BaseModel`)
# ============================================================================


class MetaConfig(BaseModel):
    """Metadata identifying the analyzed 2D game concept and balance model."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    oyun_adi: str = Field(
        ...,
        min_length=2,
        validation_alias=AliasChoices("oyun_adi", "game_title", "title"),
        description="Analyzed game concept title",
    )
    surum: str = Field(
        default="1.0.0",
        validation_alias=AliasChoices("surum", "version"),
        description="Semantic version of the balance config",
    )
    tur: str = Field(
        ...,
        min_length=5,
        validation_alias=AliasChoices("tur", "sub_genre", "genre"),
        description="2D Hyper-Casual / Hybrid-Casual sub-genre description",
    )
    tasarim_lideri: str = Field(
        default="Autonomous Game Design, Market & Thinking Lead",
        validation_alias=AliasChoices("tasarim_lideri", "design_lead", "author"),
        description="Authoring agent role",
    )
    denge_modeli: str = Field(
        ...,
        min_length=5,
        validation_alias=AliasChoices("denge_modeli", "balance_model"),
        description="Primary mathematical balance model summary",
    )
    tarih: str = Field(
        ...,
        pattern=r"^\d{4}-\d{2}-\d{2}$",
        validation_alias=AliasChoices("tarih", "date"),
        description="ISO date (YYYY-MM-DD)",
    )
    aciklama: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices("aciklama", "description"),
        description="Context description of the balance configuration",
    )


class CpiHookSummary(BaseModel):
    """Structured 3-Second Visual CPI Hook handoff for downstream GDD & Creative stages."""

    model_config = ConfigDict(extra="allow")

    hook_0_to_1_sec: str = Field(..., min_length=5, description="0-1s visual tension / pattern interrupt")
    hook_1_to_2_sec: str = Field(..., min_length=5, description="1-2s one-finger input gesture & twist")
    hook_2_to_3_sec: str = Field(..., min_length=5, description="2-3s satisfying ASMR payoff / chain reaction")


class CompetitorBenchmark(BaseModel):
    """Deconstruction of a market leader (Find stage): psychological driver, churn friction, and market gap."""

    model_config = ConfigDict(extra="allow")

    competitor_name: str = Field(..., min_length=2, description="Benchmark competitor game title")
    psychological_driver: str = Field(..., min_length=5, description="Core psychological & mechanical compulsion")
    churn_friction_point: str = Field(..., min_length=5, description="Where and why players churn in this competitor")
    exploited_market_gap: str = Field(..., min_length=5, description="How our concept solves this friction point")


class KeepKillVerdict(BaseModel):
    """Devil's Advocate Keep/Kill evaluation (Think stage) for the locked concept."""

    model_config = ConfigDict(extra="allow")

    verdict: str = Field(default="KEEP", pattern=r"^(KEEP|KILL|REFACTOR)$", description="Keep / Kill / Refactor decision")
    winning_reason: str = Field(..., min_length=5, description="Why the chosen concept survives the Keep/Kill filter")
    killed_alternatives_reason: str = Field(..., min_length=5, description="Why rejected brainstorm alternatives were killed")
    primary_churn_risk_mitigation: str = Field(..., min_length=5, description="How the #1 churn risk is mathematically mitigated")


class MdaSummary(BaseModel):
    """Structured 2D MDA handoff summary for downstream GDD stage."""

    model_config = ConfigDict(extra="allow")

    one_finger_input_schema: str = Field(..., min_length=3, description="Primary single-finger input gesture (Tap, Drag, Hold & Release, Swipe)")
    core_mechanics: str = Field(..., min_length=5, description="Core mechanical rule and win/fail condition")
    core_dynamics: str = Field(..., min_length=5, description="Tension-release pacing and risk/reward dynamics")
    core_aesthetics: str = Field(..., min_length=5, description="Primary player sensation and ASMR aesthetic payoff")


class PhysicsSimulationConfig(BaseModel):
    """Engine-neutral 2D physics simulation parameters."""

    model_config = ConfigDict(extra="allow")

    fixed_timestep_sec: float = Field(default=0.01666, gt=0.0, le=0.05, description="Fixed physics step in seconds (e.g. 0.01666 for 60Hz)")
    physics_hz: int = Field(default=60, ge=30, le=240, description="Simulation tick rate in Hz")
    continuous_collision_detection: bool = Field(default=True, description="Whether CCD is enabled to prevent fast-body tunneling")
    render_interpolation: bool = Field(default=True, description="Whether visual interpolation is enabled between physics ticks")
    gravity_scale: float = Field(default=0.0, ge=-10.0, le=10.0, description="Gravity multiplier")
    linear_drag: float = Field(default=0.0, ge=0.0, le=50.0, description="Linear velocity damping")
    restitution_bounciness: float = Field(default=0.0, ge=0.0, le=2.0, description="Collision elasticity / bounciness coefficient")
    friction: float = Field(default=0.0, ge=0.0, le=5.0, description="Surface friction coefficient")


class PhysicsAndCollisionTuning(BaseModel):
    """Container for core 2D physics simulation and concept-specific collision rules."""

    model_config = ConfigDict(extra="allow")

    simulation: PhysicsSimulationConfig = Field(default_factory=PhysicsSimulationConfig)


class LevelMilestone(BaseModel):
    """Quantified level milestone snapshot along the difficulty progression curve."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    level: int = Field(..., ge=1, description="Milestone level number (>= 1)")
    tanim_tr: str = Field(
        ...,
        min_length=5,
        validation_alias=AliasChoices("tanim_tr", "description", "summary"),
        description="Design description of the level milestone",
    )


class DifficultyProgressionCurves(BaseModel):
    """Mathematical progression formulas and concrete level milestones."""

    model_config = ConfigDict(extra="allow")

    formulas: Dict[str, str] = Field(
        ...,
        min_length=2,
        description="Mathematical progression formulas (linear, exponential, or logarithmic)",
    )
    level_milestones: List[LevelMilestone] = Field(
        ...,
        min_length=3,
        description="Concrete milestone evaluations across early, mid, and late game",
    )

    @field_validator("level_milestones")
    @classmethod
    def validate_ascending_levels(cls, milestones: List[LevelMilestone]) -> List[LevelMilestone]:
        levels = [m.level for m in milestones]
        if levels != sorted(levels):
            raise ValueError(f"level_milestones must be ordered in ascending level order, got {levels}")
        return milestones


class ScreenShakeTraumaConfig(BaseModel):
    """Quadratic camera trauma model (`Shake = Trauma^2`)."""

    model_config = ConfigDict(extra="allow")

    model: str = Field(..., min_length=5, description="Mathematical screen shake model specification")
    trauma_decay_per_sec: float = Field(..., gt=0.0, le=10.0, description="Linear trauma decay rate per second")
    max_offset_pixels: List[float] = Field(
        ...,
        min_length=2,
        max_length=2,
        description="Maximum [X, Y] translational camera shake offset in pixels",
    )
    max_rotation_radians: float = Field(..., ge=0.0, le=1.0, description="Maximum rotational shake angle in radians")
    noise_frequency_hz: float = Field(..., gt=0.0, le=120.0, description="Perlin/Simplex or sinusoidal shake frequency in Hz")
    event_trauma_increments: Dict[str, float] = Field(
        ...,
        min_length=2,
        description="Normalized trauma increments [0.0 - 1.0] added per gameplay event",
    )

    @field_validator("event_trauma_increments")
    @classmethod
    def validate_trauma_range(cls, increments: Dict[str, float]) -> Dict[str, float]:
        for event_name, val in increments.items():
            if not (0.0 <= val <= 1.0):
                raise ValueError(f"Trauma increment '{event_name}' must be within [0.0, 1.0], got {val}")
        return increments


class HitStopTierConfig(BaseModel):
    """Single hit-stop / freeze-frame tier specification."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    duration_realtime_sec: float = Field(
        ...,
        ge=0.0,
        le=0.5,
        description="Real-time hit-stop duration in seconds (0ms to 500ms)",
    )
    time_scale: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Engine time scale during hit-stop (0.0 = full freeze, 1.0 = normal speed)",
    )
    tanim_tr: str = Field(
        ...,
        min_length=3,
        validation_alias=AliasChoices("tanim_tr", "description", "trigger"),
        description="Explanation of when this hit-stop tier triggers",
    )


class SquashAndStretchConfig(BaseModel):
    """Squash & Stretch deformation vectors and tween restoration curves."""

    model_config = ConfigDict(extra="allow")

    tween_ease_type: str = Field(..., min_length=3, description="Easing function name (e.g. EaseOutBack, EaseOutElastic)")
    tween_restore_duration_sec: float = Field(..., gt=0.0, le=1.0, description="Duration to restore scale to [1.0, 1.0] in seconds")


class SidechainDuckingConfig(BaseModel):
    """Audio bus sidechain ducking parameters (`audio-design` discipline)."""

    model_config = ConfigDict(extra="allow")

    trigger_bus: str = Field(..., min_length=2, description="Bus that triggers ducking (e.g. SFX_Glass, SFX_Impacts)")
    target_bus: str = Field(..., min_length=2, description="Bus being ducked (e.g. Music)")
    duck_gain_db: float = Field(..., lt=0.0, ge=-48.0, description="Gain reduction in dB (must be negative)")
    attack_ms: float = Field(..., gt=0.0, le=500.0, description="Ducking attack time in milliseconds")
    release_ms: float = Field(..., gt=0.0, le=2000.0, description="Ducking release time in milliseconds")


class AudioDesignAndMixingConfig(BaseModel):
    """Optional audio bus hierarchy, loudness normalization, and harmonic pitch rules."""

    model_config = ConfigDict(extra="allow")

    bus_hierarchy: List[str] = Field(default_factory=lambda: ["Master", "Music", "SFX", "UI"], min_length=2, description="Ordered audio mixer bus list")
    master_target_loudness_lufs: float = Field(default=-14.0, le=0.0, ge=-30.0, description="Target master loudness in LUFS (typically -14.0)")
    sidechain_ducking: Optional[SidechainDuckingConfig] = Field(default=None, description="Optional sidechain ducking settings")


class JuiceAndGameFeelMatrix(BaseModel):
    """Complete quantified 2D Game Feel & Juice choreography matrix."""

    model_config = ConfigDict(extra="allow")

    screen_shake_trauma: ScreenShakeTraumaConfig
    hit_stop_freeze_frames: Dict[str, HitStopTierConfig] = Field(
        ...,
        min_length=2,
        description="Multi-tier hit-stop freeze frame definitions",
    )
    squash_and_stretch: SquashAndStretchConfig
    particle_choreography: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict,
        description="Particle burst emission definitions per gameplay event",
    )
    audio_design_and_mixing: Optional[AudioDesignAndMixingConfig] = Field(
        default=None,
        description="Optional audio mixing and ASMR frequency parameters",
    )


class ScoringAndComboEconomy(BaseModel):
    """Scoring rewards and combo escalation window parameters."""

    model_config = ConfigDict(extra="allow")

    combo_multiplier_step: float = Field(..., gt=0.0, le=5.0, description="Multiplier increment per combo step")
    max_combo_multiplier: float = Field(..., gt=1.0, le=100.0, description="Maximum cap on combo multiplier")


class GameBalanceConfig(BaseModel):
    """
    Root Pydantic v2 Data Contract for `game_balance.json`.

    Validates all mandatory studio pipeline sections while allowing concept-specific
    mechanic blocks (e.g., `player_sling_and_pulse_mechanics`, `slicing_mechanics`,
    `sorting_grid_mechanics`) via structured dictionary validation.
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    meta: MetaConfig
    cpi_hook_summary: Optional[CpiHookSummary] = Field(
        default=None,
        description="Structured 3-second visual CPI hook handoff for GDD stage",
    )
    competitor_benchmarks: Optional[List[CompetitorBenchmark]] = Field(
        default=None,
        min_length=2,
        description="2-3 deconstructed competitor benchmarks (Find stage)",
    )
    keep_kill_verdict: Optional[KeepKillVerdict] = Field(
        default=None,
        description="Devil's Advocate Keep/Kill evaluation summary (Think stage)",
    )
    mda_summary: Optional[MdaSummary] = Field(
        default=None,
        description="Structured 2D MDA handoff summary for GDD stage",
    )
    physics_and_collision_tuning: PhysicsAndCollisionTuning = Field(
        ...,
        validation_alias=AliasChoices("physics_and_collision_tuning", "physics_tuning", "physics"),
    )
    difficulty_progression_curves: DifficultyProgressionCurves = Field(
        ...,
        validation_alias=AliasChoices("difficulty_progression_curves", "difficulty_progression", "progression_curves"),
    )
    juice_and_game_feel_matrix: JuiceAndGameFeelMatrix = Field(
        ...,
        validation_alias=AliasChoices("juice_and_game_feel_matrix", "juice_matrix", "game_feel_matrix"),
    )
    scoring_and_combo_economy: ScoringAndComboEconomy = Field(
        ...,
        validation_alias=AliasChoices("scoring_and_combo_economy", "scoring_economy", "scoring"),
    )

    @model_validator(mode="after")
    def validate_concept_mechanics_present(self) -> "GameBalanceConfig":
        extra_keys = set(self.__pydantic_extra__.keys()) if self.__pydantic_extra__ else set()
        if not extra_keys:
            raise ValueError(
                "game_balance.json must include at least one concept-specific mechanics section "
                "(e.g., 'player_sling_and_pulse_mechanics' or 'core_mechanics')."
            )
        return self


# ============================================================================
# 2. CLI VALIDATION RUNNER
# ============================================================================


def resolve_default_balance_path(root_dir: Path) -> Path:
    cwd_balance = Path.cwd() / "game_balance.json"
    return cwd_balance if cwd_balance.exists() else root_dir / "game_balance.json"


def main() -> int:
    root_dir = Path(__file__).resolve().parent
    target_path = (
        Path(sys.argv[1])
        if len(sys.argv) > 1 and not sys.argv[1].startswith("--")
        else resolve_default_balance_path(root_dir)
    )

    if not target_path.exists():
        print("✅ Pydantic v2 Schema Contract Ready (`GameBalanceConfig` in `validate_balance.py`)!")
        print(f"   • Total Validated Models : 16 Pydantic BaseModel classes")
        print("   • Status                 : No `game_balance.json` generated yet. Run `/analyze` to generate and validate a balance file.")
        return 0

    try:
        raw_data = json.loads(target_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[ERROR] Invalid JSON syntax in {target_path}: {exc}", file=sys.stderr)
        return 1

    try:
        validated = GameBalanceConfig.model_validate(raw_data)
    except ValidationError as exc:
        print(f"[FAILED] Pydantic validation failed for {target_path}:\n", file=sys.stderr)
        print(exc, file=sys.stderr)
        return 1

    extra_sections = list(validated.__pydantic_extra__.keys()) if validated.__pydantic_extra__ else []
    print("✅ Pydantic v2 Validation PASSED!")
    print(f"   • File Validated  : {target_path}")
    print(f"   • Game Title      : {validated.meta.oyun_adi} (v{validated.meta.surum})")
    print(f"   • Sub-Genre       : {validated.meta.tur}")
    print(f"   • Mechanic Blocks : {', '.join(extra_sections)}")
    print(f"   • Physics Rate    : {validated.physics_and_collision_tuning.simulation.physics_hz} Hz (CCD={validated.physics_and_collision_tuning.simulation.continuous_collision_detection})")
    print(f"   • Formulas Count  : {len(validated.difficulty_progression_curves.formulas)}")
    print(f"   • Milestones      : {len(validated.difficulty_progression_curves.level_milestones)} levels validated")
    print(f"   • Hit-Stop Tiers  : {len(validated.juice_and_game_feel_matrix.hit_stop_freeze_frames)} tiers validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
