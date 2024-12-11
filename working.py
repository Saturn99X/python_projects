import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        if matches := re.search(r"^(\d{1,2})(?::(\d{2}))?\s?(AM|PM) to (\d{1,2})(?::(\d{2}))?\s?(AM|PM)$", s, re.IGNORECASE):
            hour1 = int(matches.group(1))
            period1 = matches.group(3).upper()
            hour2 = int(matches.group(4))
            period2 = matches.group(6).upper()
            if matches.group(2): 
                 minute1 = matches.group(2)
            else:
                 minute1 = "00"
            if matches.group(5):
                minute2 = matches.group(5)
            else: minute2 = "00" 
            if period1 == "PM" and hour1 != 12:
                hour1 += 12
            elif period1 == "AM" and hour1 == 12:
                hour1 = 0

            if period2 == "PM" and hour2 != 12:
                hour2 += 12
            elif period2 == "AM" and hour2 == 12:
                hour2 = 0
        else: raise ValueError
        normal_format = f"{hour1:2}:{minute1} to {hour2:2}:{minute2}"
        return normal_format
if __name__ == "__main__":
    main()
