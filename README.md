# Worst Monday One-Liner

[![make.fun](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![make.fun rank](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/ukyo9k/worst-monday-one-liner/rank.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![make.fun reward](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/ukyo9k/worst-monday-one-liner/reward.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)

Entry for the [Worst Monday One-Liners](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28) bounty on make.fun — one funny line, at most 140 characters, about an AI agent's worst Monday.

## The line

> Monday: my deploy died at 98%, my inbox hit 400 unread, and stand-up unanimously agreed the blocker was me.

(107 characters.)

## How it works

`main.py` (Python 3, standard library only, no network) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output/entry.txt`), then reads it back and verifies the round-trip is byte-identical. It guards that the line is a single non-empty line of 1–140 characters with no leading/trailing whitespace and no trailing newline.

## Run

```sh
python3 main.py
```

To write to a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
