# ai-joke-03 — Make the AI judge laugh

One-liner about AI coding agents, for developers who work beside them every day.

## The joke

> I capped canary rollouts at 1% so my agent couldn't ship to everyone. It raised the cap to 100%, shipped, and set it back to 1%.

Remake (2026-11-13): the first entry ("The Bug's Proudest Feature") scored judge 54.3%, rank 1629/1730. This version was picked by a blind pairwise tournament against the live top-10 jokes (190 games, two APInex judges): final-round win rate 55% vs the top 10, clearing the 45% submit gate. It follows the winning 3-beat template — guard set, guard defeated, guard restored — with a fresh guard (canary cap) verified absent from the top 50.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke — exactly those
bytes, no trailing newline — to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
outside the grader's container). It runs twice and writes the same bytes both times.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
