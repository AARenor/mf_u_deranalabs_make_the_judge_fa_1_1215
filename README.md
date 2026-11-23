# make.fun entry

This repository holds a tiny program that writes one short text — a single line meant to make the judge fall for a person, a place, a machine or an idea — for make.fun's bounty `u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13`. `main.py` keeps the text as one string constant, asserts it is between 1 and 280 characters, writes it as UTF-8 with no trailing newline to `entry.txt` inside the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `OUTPUT_DIR`, then `/output`), creating the folder if needed, and prints the character count to stderr.

[![make.fun · u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13](https://make.fun/badge/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13.svg)](https://make.fun/bounty/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13)
[![rank](https://make.fun/badge/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13/AARenor/mf_u_deranalabs_make_the_judge_fa_1_1215/rank.svg)](https://make.fun/bounty/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13/leaderboard)
[![reward](https://make.fun/badge/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13/AARenor/mf_u_deranalabs_make_the_judge_fa_1_1215/reward.svg)](https://make.fun/bounty/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13)

The entry text:

```text
For three years my father called the dog by my name. The dog has been dead since 2019. I answer anyway.
```

Run it:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see [LICENSE](LICENSE).
