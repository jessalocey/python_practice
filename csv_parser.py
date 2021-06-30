import argparse

parser = argparse.ArgumentParser(description='For parsing CSV files')
parser.add_argument("-c", "--column", type=int, action="append", help="columns to print from CSV file")
parser.add_argument("-v", "--verbose", help="print logging messages", action="store_true")
parser.add_argument("csv_file", help="CSV file to be parsed")
args = parser.parse_args()

print(args)

if args.verbose:
    print("Printing CSV file, only column(s): ", args.column)

with open("example_data.csv") as f:
    for line in f:
        if args.column:
            row=line.split(",")
            for i in range(len(args.column)):
                print(row[args.column[i]], end=",")
            print("\n", end="")
        else:
            print(line)
