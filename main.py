# ai-joke-03 entry: writes one joke about AI coding agents to /output/entry.txt.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The joke, exactly as the judge will read it: one line, no trailing newline.
JOKE = "I asked for a bug fix; the agent shipped a feature that makes the bug proud."

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
