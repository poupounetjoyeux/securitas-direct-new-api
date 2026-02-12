"""Define constants for Securitas Direct API."""

from enum import StrEnum


class CommandType(StrEnum):
    """Legacy command type enum - kept for migration from old config."""
    STD = "std"
    PERI = "peri"


class SecuritasState(StrEnum):
    """Verisure alarm states - combinations of interior mode and perimeter."""
    NOT_USED = "not_used"
    DISARMED = "disarmed"
    PARTIAL = "partial"
    TOTAL = "total"
    PERI_ONLY = "peri_only"
    PARTIAL_PERI = "partial_peri"
    TOTAL_PERI = "total_peri"


# Map SecuritasState -> API arm command string
STATE_TO_COMMAND: dict[SecuritasState, str] = {
    SecuritasState.DISARMED: "DARM1DARMPERI",
    SecuritasState.PARTIAL: "ARMDAY1",
    SecuritasState.TOTAL: "ARM1",
    SecuritasState.PERI_ONLY: "PERI1",
    SecuritasState.PARTIAL_PERI: "ARMDAY1PERI1",
    SecuritasState.TOTAL_PERI: "ARM1PERI1",
}

# Map protomResponse code -> SecuritasState
PROTO_TO_STATE: dict[str, SecuritasState] = {
    "D": SecuritasState.DISARMED,
    "E": SecuritasState.PERI_ONLY,
    "P": SecuritasState.PARTIAL,
    "B": SecuritasState.PARTIAL_PERI,
    "T": SecuritasState.TOTAL,
    "A": SecuritasState.TOTAL_PERI,
}

# Human-readable labels for the config UI
STATE_LABELS: dict[SecuritasState, str] = {
    SecuritasState.DISARMED: "Disarmed",
    SecuritasState.PARTIAL: "Partial",
    SecuritasState.TOTAL: "Total",
    SecuritasState.PERI_ONLY: "Perimeter only",
    SecuritasState.PARTIAL_PERI: "Partial + Perimeter",
    SecuritasState.TOTAL_PERI: "Total + Perimeter",
}

# Options available when perimeter is NOT configured
STD_OPTIONS: list[SecuritasState] = [
    SecuritasState.DISARMED,
    SecuritasState.PARTIAL,
    SecuritasState.TOTAL,
]

# Options available when perimeter IS configured
PERI_OPTIONS: list[SecuritasState] = [
    SecuritasState.DISARMED,
    SecuritasState.PARTIAL,
    SecuritasState.TOTAL,
    SecuritasState.PERI_ONLY,
    SecuritasState.PARTIAL_PERI,
    SecuritasState.TOTAL_PERI,
]

# Default mappings matching current behavior (keyed by HA button name)
STD_DEFAULTS: dict[str, SecuritasState] = {
    "map_home": SecuritasState.PARTIAL,
    "map_away": SecuritasState.TOTAL,
    "map_night": SecuritasState.PARTIAL,
    "map_custom": SecuritasState.NOT_USED,
}

PERI_DEFAULTS: dict[str, SecuritasState] = {
    "map_home": SecuritasState.PARTIAL,
    "map_away": SecuritasState.TOTAL_PERI,
    "map_night": SecuritasState.PARTIAL_PERI,
    "map_custom": SecuritasState.PERI_ONLY,
}
