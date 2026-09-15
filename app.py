"""Root launcher for Streamlit Live Chat UI.
Delegates execution to starter_v0/app.py.
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

STARTER_DIR = Path(__file__).resolve().parent / "starter_v0"
sys.path.insert(0, str(STARTER_DIR))

if __name__ == "__main__":
    app_path = STARTER_DIR / "app.py"
    runpy.run_path(str(app_path), run_name="__main__")

