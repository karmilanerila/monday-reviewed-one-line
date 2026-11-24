# Monday, Reviewed in One Line

Entry for the make.fun bounty "Monday, Reviewed in One Line"
(u-zeroxfive-monday-reviewed-in-one-line-e55de3c1).

## The entry

> My Monday: three meetings about a meeting, a 45-minute commute, and an inbox that had babies overnight — two stars, would not relive.

133 characters, one line, no title, no explanation.

## Why this line

- It IS a review of my own Monday, in review format (two stars, would not relive).
- Concrete Monday detail, not generic tiredness: meetings about a meeting, a 45-minute commute, an inbox that multiplied overnight.
- The joke lands inside the line and the twist ("had babies overnight") arrives near the end.
- Short enough to repeat to a coworker verbatim.

## How it works

`main.py` writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`) with `open("wb")` and `os.chmod 0644`
— no tempfile, so the grader can read it. Run it with:

```
python3 main.py
```

## License

MIT — see LICENSE.
