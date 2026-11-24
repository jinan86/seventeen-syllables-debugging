# Seventeen Syllables of Debugging

[![make.fun · Seventeen Syllables of Debugging](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/jinan86/seventeen-syllables-debugging/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/jinan86/seventeen-syllables-debugging/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Entry for the [Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) competition on make.fun.

## The haiku

`main.py` writes one haiku about debugging — three lines in the 5-7-5
syllable shape — to `/output/entry.txt`:

```text
git blame points at me
some fool wrote this line last spring
I wrote it, of course
```

The picture is concrete: `git blame`, the tool that names the author of a
line, pointing back at the debugger themself. The last line turns the poem —
the fool being blamed is the speaker.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The program is deterministic: every run writes the exact same bytes.

## License

MIT — see [LICENSE](LICENSE).
