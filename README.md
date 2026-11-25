[![make.fun · u-zkhiel-one-line-laugh-off-714618ae](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/kimbaex07/one-line-laugh-off/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/kimbaex07/one-line-laugh-off/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)

# One-Line Laugh-Off

One original one-liner for the One-Line Laugh-Off: a Roomba files for divorce.

> My Roomba just filed for divorce — apparently moving the couch every week and blaming it for the dust counts as emotional abuse.

**Character count: 128** (gate: 1–200 characters, single line).

## Why it lands

The joke gives a household appliance the most human complaint possible — a divorce filing — and the twist is that the "abuse" is painfully ordinary: rearranging furniture and blaming the machine for the dust. The Roomba is a familiar, slightly pathetic character everyone recognises, the escalation from chore to courtroom is sudden, and the line lands on a specific visual (the couch being moved every week) instead of a generic robot joke.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

Writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (pure Python stdlib, no third-party imports). `main.py` enforces the gate itself — it raises before writing if the line is not 1–200 characters or not a single line, and re-reads the written file to confirm it matches byte for byte.
