import argparse #need this to parse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foo", action="append", help="foo help") #can have type=int, default="hi"
args = parser.parse_args()

print(args)