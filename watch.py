import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"(https?://)(www.)?(youtu)(be)\.(com)/embed/(xvFZjo5PgG0)", s, re.IGNORECASE):
        url = f"{matches.group(1)}{matches.group(3)}.{matches.group(4)}/{matches.group(6)}"
    return url



if __name__ == "__main__":
    main()
