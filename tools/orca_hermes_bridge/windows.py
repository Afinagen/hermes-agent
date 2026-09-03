"""Small Windows lifecycle primitives used by the bridge."""

from __future__ import annotations

import subprocess


def hidden_process_flags() -> int:
    """Return creation flags that keep short-lived bridge helpers invisible."""
    return int(getattr(subprocess, "CREATE_NO_WINDOW", 0))
