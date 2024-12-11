import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    i = 0
    word_to_find = "um"
    pattern = rf"\b{re.escape(word_to_find)}\b"
    for _ in range(len(s)):
        matches = re.findall(pattern, s, re.IGNORECASE)
        if matches :
            return f"{len(matches)}"
if __name__ == "__main__":
    main()
