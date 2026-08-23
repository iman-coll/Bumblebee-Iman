"""Low-resource Streamlit entry point for Iman's Pakistan History Quiz.

The quiz source remains in Bumblebee_quiz_app/app.py. This launcher removes
resource-heavy visual effects before execution, keeps the animation self-contained,
and caches only the compiled Python source. No external image or API is requested.
"""
from pathlib import Path
import streamlit as st

APP_DIR = Path(__file__).resolve().parent / "Bumblebee_quiz_app"
SOURCE = APP_DIR / "app.py"

if not SOURCE.exists():
    st.error("Quiz source file is missing: Bumblebee_quiz_app/app.py")
    st.stop()

# A small inline SVG keeps the visual element local and avoids remote image traffic.
SELF_CONTAINED_SVG = (
    "data:image/svg+xml;utf8,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'%3E"
    "%3Crect x='12' y='10' width='176' height='180' rx='22' fill='%232d3744' stroke='%23ffd700' stroke-width='4'/%3E"
    "%3Crect x='28' y='28' width='144' height='118' rx='14' fill='%23101822' stroke='%2399a8b8' stroke-width='3'/%3E"
    "%3Ccircle cx='100' cy='87' r='42' fill='%233e5366' stroke='%23d9e2ec' stroke-width='5'/%3E"
    "%3Ccircle cx='100' cy='87' r='29' fill='%23101a26' stroke='%237f8c99' stroke-width='3'/%3E"
    "%3Ccircle cx='100' cy='87' r='9' fill='%23ffd700'/%3E"
    "%3Ccircle cx='45' cy='163' r='6' fill='%23ff5c5c'/%3E"
    "%3Ccircle cx='65' cy='163' r='6' fill='%23ffd700'/%3E"
    "%3Ccircle cx='85' cy='163' r='6' fill='%2355d66b'/%3E"
    "%3C/svg%3E"
)


@st.cache_resource(show_spinner=False)
def load_quiz_source():
    source = SOURCE.read_text(encoding="utf-8")

    # Localize the image.
    source = source.replace(
        "https://picsum.photos/seed/laundromat/200/200",
        SELF_CONTAINED_SVG,
    )

    # Disable the continuously running CSS animations. They run in the browser,
    # but removing them makes the deployed app substantially lighter for users.
    source = source.replace("animation: flyAcross 20s linear infinite;", "")
    source = source.replace("animation: vibrate 0.5s infinite;", "")
    source = source.replace("backdrop-filter: blur(10px);", "")
    source = source.replace("filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.5));", "")
    source = source.replace("st.balloons()", "# balloons disabled for low-resource deployment")

    # Remove the unused random import from the original source.
    source = source.replace("import random\n", "")

    return compile(source, str(SOURCE), "exec")


# Streamlit reruns this entry point after widget interaction. The expensive
# file-read/compile work is cached, while the quiz itself retains its normal
# session-state behaviour.
exec(
    load_quiz_source(),
    {"__name__": "__main__", "__file__": str(SOURCE)},
)
