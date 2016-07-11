
import os
import sys
import itertools
import argparse

parser = argparse.ArgumentParser(description='This program alternately writes lines of two source files into new destination')
parser.add_argument(help='Valid path to the first source file',dest='right')
parser.add_argument(help='Valid path to the second source file',dest='left')
parser.add_argument(help='Valid path to create destination file there',dest='dest')
args = parser.parse_args()

if os.path.isfile(args.dest):
	sys.exit("File {0} already exists".format(args.dest))

with open(args.right, 'r') as fright:
	with open(args.left,'r') as fleft:
		with open(args.dest,'w') as fout:
			for item in itertools.izip_longest(fright, fleft):
				if item[0]:
					fout.write(item[0])
				if item[1]:
					fout.write(item[1])


