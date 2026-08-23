"""Streamlit entry point for the Bumblebee Pakistan History Quiz.

The original quiz lives in Bumblebee_quiz_app/app.py. This lightweight launcher
keeps that code as the single quiz source while replacing its remote animation
image with an embedded SVG. The compiled source is cached so every Streamlit
rerun does not repeatedly read/compile the large quiz file.
"""
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parent / "Bumblebee_quiz_app"
SOURCE = APP_DIR / "app.py"

if not SOURCE.exists():
    raise FileNotFoundError(f"Quiz application not found: {SOURCE}")

# Local SVG: no external image request and no dependency on Picsum.
SELF_CONTAINED_SVG = (
    "data:image/svg+xml;utf8,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'%3E"
    "%3Cdefs%3E%3CradialGradient id='g' cx='50%25' cy='45%25' r='60%25'%3E"
    "%3Cstop offset='0' stop-color='%235c6b7a'/%3E"
    "%3Cstop offset='1' stop-color='%23151b23'/%3E%3C/radialGradient%3E%3C/defs%3E"
    "%3Crect x='12' y='10' width='176' height='180' rx='22' fill='%232d3744' stroke='%23ffd700' stroke-width='4'/%3E"
    "%3Crect x='28' y='28' width='144' height='118' rx='14' fill='%23101822' stroke='%2399a8b8' stroke-width='3'/%3E"
    "%3Ccircle cx='100' cy='87' r='42' fill='url(%23g)' stroke='%23d9e2ec' stroke-width='5'/%3E"
    "%3Ccircle cx='100' cy='87' r='29' fill='%23101a26' stroke='%237f8c99' stroke-width='3'/%3E"
    "%3Ccircle cx='100' cy='87' r='9' fill='%23ffd700' opacity='.85'/%3E"
    "%3Ccircle cx='45' cy='163' r='6' fill='%23ff5c5c'/%3E"
    "%3Ccircle cx='65' cy='163' r='6' fill='%23ffd700'/%3E"
    "%3Ccircle cx='85' cy='163' r='6' fill='%2355d66b'/%3E"
    "%3Cpath d='M118 163h43' stroke='%2399a8b8' stroke-width='6' stroke-linecap='round'/%3E"
    "%3C/svg%3E"
)


@st.cache_resource(show_spinner=False)
def get_compiled_app():
    """Read, replace the remote image, and compile the quiz source once."""
    source = SOURCE.read_text(encoding="utf-8")
    source = source.replace(
        "https://picsum.photos/seed/laundromat/200/200",
        SELF_CONTAINED_SVG,
    )
    return compile(source, str(SOURCE), "exec")


# Run the original quiz. Streamlit reruns the execution state normally, while
# the expensive file-read/compile step above stays cached for the process.
exec(
    get_compiled_app(),
    {"__name__": "__main__", "__file__": str(SOURCE)},
)
