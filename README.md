# ai-joke-03 — Make the AI judge laugh

One-liner about AI coding agents, for developers who work beside them every day.

## The joke

> I asked for a bug fix; the agent shipped a feature that makes the bug proud.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke — exactly those
bytes, no trailing newline — to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
outside the grader's container). It runs twice and writes the same bytes both times.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
