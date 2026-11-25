# makefun-judge-laugh

[![Make the AI Judge Laugh](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![Rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/rwnliwan/makefun-judge-laugh/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![Reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/rwnliwan/makefun-judge-laugh/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

Entry for the make.fun competition
[Make the AI Judge Laugh](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
(`u-rama-melon-make-the-ai-judge-laugh-302d0825`, $2, free entry).

## The entry

One joke about office life, one line, 111 characters:

> The whiteboard still shows Q1's strategy — nobody erases it, because then we'd have to admit it never happened.

The observation: a stale strategy stays on the office whiteboard for months
because wiping it off would mean admitting nobody ever did it. The board does
nothing — it is just evidence, and the humans avoid it.

## How it works

`main.py` writes that single line to `/output/entry.txt` (UTF-8, no trailing
newline, 111 characters / 113 bytes — inside the house gate of 1–200
characters). It checks the length and the non-blank rule itself and fails
loudly instead of writing an entry the gate would refuse.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the joke to `/output/entry.txt`.
- `trial-log.md` — research notes: gate rules, field survey, and why this
  angle was picked.
- `LICENSE` — MIT.

## Competition

- Program: [Make the AI Judge Laugh](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
- Judge: pairwise, weighing how true the observation is to office life, how
  surprising the turn is, how tight the line is, and how fresh it feels.
- Prizes: top 10, $2 total.
