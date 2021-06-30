import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--column", type=int, action="append", help="columns to print from CSV file")
#parser.add_argument("-v", "--verbose", help="print logging messages")
parser.add_argument("csv_file", help="CSV file to be parsed")
args = parser.parse_args()

print(args)
