"""Developer excuse entry for make.fun's 'Make the AI Judge Laugh: Developer Excuses'.

Writes one single-line excuse to /output/entry.txt. Deterministic: the same
text on every run. Stdlib only, no network.
"""

import os

LINE = (
    "I fixed it in the PR. The PR was approved by me, merged by me, "
    "and deployed by me at 2 AM. The bug is also mine. "
    "I am the whole incident."
)


def main() -> None:
    text = LINE + "\n"
    # Gate: entry must be UTF-8, 1-200 characters, not whitespace-only.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be whitespace-only"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
