from __future__ import annotations

import sys
from pathlib import Path

# Ensure the ``src`` directory is importable when the package is not installed.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))
