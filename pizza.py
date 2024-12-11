import sys
import csv
from tabulate import tabulate

filename = sys.argv[1]

if len(sys.argv) == 2:
    if filename.endswith(".csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                data = list(reader)
                print(tabulate(data, tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("The file doesn't exist")
    elif len(sys.argv) < 2:
        sys.exit("too few command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("too many command-line argument")
    else:
        sys.exit("the file is not a csv file")