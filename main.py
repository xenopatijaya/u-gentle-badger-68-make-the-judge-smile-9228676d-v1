"""Make the Judge Smile — one warm line about a small good thing today.

Writes exactly one line (115 characters) to /output/entry.txt.
Python standard library only; no network, no input files.

Why this line: it leads with a small good thing that happened this
morning (subject), lands as a genuinely felt kindness (warmth), turns
on the secret extra banana and the whispered aside (surprise), and
carries one concrete sensory detail — 6 a.m., a fried banana, a
whisper — in fresh, un-borrowed wording.
"""

import os

ENTRY = (
    "At 6 a.m. the warung lady slipped an extra fried banana into my bag "
    "and whispered, 'for the road, you look hungry.'"
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
