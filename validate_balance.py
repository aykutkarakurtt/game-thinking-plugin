#!/usr/bin/env python3
"""
CLI Validator & JSON Schema Exporter for `game_balance.json` using Pydantic v2.

Usage:
    python3 validate_balance.py [path_to_game_balance.json] [--export-schema]
"""

import json
import sys
from pathlib import Path
from pydantic import ValidationError

from schemas.game_balance_schema import GameBalanceConfig


def main() -> int:
    root_dir = Path(__file__).resolve().parent
    cwd_balance = Path.cwd() / "game_balance.json"
    default_balance = cwd_balance if cwd_balance.exists() else root_dir / "game_balance.json"
    target_path = Path(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else default_balance
    export_schema_path = root_dir / "schemas" / "game_balance.schema.json"

    # Always keep the exported JSON Schema up to date for downstream GDD / Studio agents
    schema_dict = GameBalanceConfig.model_json_schema()
    export_schema_path.write_text(
        json.dumps(schema_dict, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    if not target_path.exists():
        print("✅ Pydantic v2 Schema Contract Ready (`GameBalanceConfig`)!")
        print(f"   • JSON Schema     : Exported to {export_schema_path.relative_to(root_dir)}")
        print(f"   • Status          : No `{target_path.name}` generated yet. Run `/analyze` to generate and validate a balance file.")
        return 0

    try:
        raw_data = json.loads(target_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[ERROR] Invalid JSON syntax in {target_path}: {exc}", file=sys.stderr)
        return 1

    try:
        validated = GameBalanceConfig.model_validate(raw_data)
    except ValidationError as exc:
        print(f"[FAILED] Pydantic validation failed for {target_path.name}:\n", file=sys.stderr)
        print(exc, file=sys.stderr)
        return 1

    extra_sections = list(validated.__pydantic_extra__.keys()) if validated.__pydantic_extra__ else []
    print("✅ Pydantic v2 Validation PASSED!")
    print(f"   • Game Title      : {validated.meta.oyun_adi} (v{validated.meta.surum})")
    print(f"   • Sub-Genre       : {validated.meta.tur}")
    print(f"   • Mechanic Blocks : {', '.join(extra_sections)}")
    print(f"   • Physics Rate    : {validated.physics_and_collision_tuning.simulation.physics_hz} Hz (CCD={validated.physics_and_collision_tuning.simulation.continuous_collision_detection})")
    print(f"   • Formulas Count  : {len(validated.difficulty_progression_curves.formulas)}")
    print(f"   • Milestones      : {len(validated.difficulty_progression_curves.level_milestones)} levels validated")
    print(f"   • Hit-Stop Tiers  : {len(validated.juice_and_game_feel_matrix.hit_stop_freeze_frames)} tiers validated")
    print(f"   • JSON Schema     : Exported to {export_schema_path.relative_to(root_dir)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
