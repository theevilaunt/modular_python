import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("--verbosity", help="increase verbosity")
args = parser.parse_args()
if args.verbosity:
	print("verbosity enabled")
#print(args.square**2)