"""The Funniest Office Joke, Judged Head to Head — entry.

Writes a single one-line office joke to /output/entry.txt.
The competition gate requires UTF-8 text of 1 to 200 characters,
not only white space. The program is deterministic: every run
writes exactly the same bytes.

For local verification only, the output path may be redirected with
the ENTRY_OUTPUT_PATH environment variable; the grader sets nothing
and gets the default /output/entry.txt.
"""

import os

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

JOKE = (
    "One reply-all reached 12,000 staff asking to be removed; 400 people "
    "replied-all 'same here', and IT logged it as our best collaboration "
    "of the quarter."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    output_path = os.environ.get("ENTRY_OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
