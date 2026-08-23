"""Streamlit entry point for the Bumblebee Pakistan History Quiz.

This root launcher keeps the original quiz in Bumblebee_quiz_app/app.py while making
its animated laundromat graphic completely self-contained. No external image host
is required at runtime.
"""
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent / "Bumblebee_quiz_app"
SOURCE = APP_DIR / "app.py"

if not SOURCE.exists():
    raise FileNotFoundError(f"Quiz application not found: {SOURCE}")

source = SOURCE.read_text(encoding="utf-8")

# Replace the old remote Picsum background with an inline SVG data URI.
# The SVG is embedded in the Python source, so Streamlit Cloud does not need
# an internet request to display the animated machine.
self_contained_svg = (
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

old_url = "https://picsum.photos/seed/laundromat/200/200"
source = source.replace(old_url, self_contained_svg)

# Execute the original app as the Streamlit entry point.
# The original quiz questions and UI remain unchanged except for the local graphic.
exec(compile(source, str(SOURCE), "exec"), {"__name__": "__main__", "__file__": str(SOURCE)})
