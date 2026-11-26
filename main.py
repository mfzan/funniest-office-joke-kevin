"""Entry for make.fun: The Funniest Office Joke, Judged Head to Head.

Writes one line -- a single office joke -- to /output/entry.txt.

The joke: the daily standup is the one meeting where everybody stays on
their feet, and the punchline is why: sitting down would be an admission
that the "fifteen-minute" meeting actually runs an hour. Setup first,
turn last, one line, no network, no randomness.
"""

import os

JOKE = (
    "The daily standup is the only meeting where everyone stands, "
    "because sitting down would admit it lasts an hour."
)

OUTPUT_PATH = "/output/entry.txt"

# The sealed scorer only accepts 1-200 characters, one line, not only
# whitespace. Refuse to write anything outside that gate rather than
# shipping an entry the judge never sees.
MAX_CHARS = 200


def main() -> int:
    if not JOKE.strip() or "\n" in JOKE or len(JOKE) > MAX_CHARS:
        raise ValueError("joke fails the 1-200 character single-line gate")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
