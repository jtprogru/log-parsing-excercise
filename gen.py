#!/usr/bin/env python3
"""
Generate some testing log-file
"""

import os
import random
from datetime import datetime, timedelta

words = [
    "alpha",
    "bravo",
    "charlie",
    "delta",
    "echo",
    "foxtrot",
    "golf",
    "hotel",
    "india",
    "juliet",
    "kilo",
    "lima",
    "mike",
    "november",
    "oscar",
    "papa",
    "quebec",
    "romeo",
    "sierra",
    "tango",
    "unifrom",
    "viktor",
    "whiskey",
    "x-ray",
    "yankee",
    "zulu",
]


def random_word():
    """
    Return random word from words
    """
    return random.choice(words)


def main():
    """
    Main function
    """
    os.makedirs("logs", exist_ok=True)

    for file in range(1, 21):
        with open(f"logs/{file}.log", "w") as fh:
            time = datetime.now()
            for _ in range(1, 101):
                fh.write(time.strftime("%Y%m%d%H%M%S "))
                fh.write(" ".join(random_word() for _ in range(10)))
                fh.write("\n")
                time += timedelta(seconds=random.randint(0, 10000))


if __name__ == "__main__":
    main()
