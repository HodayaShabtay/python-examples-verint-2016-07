"""
This program prints all anagrams in a given file
"""


import sys
import os
import argparse
import collections

parser = argparse.ArgumentParser(description='This program print all anagrams in a given file')
parser.add_argument(help='Valid path to words file',dest='file')
args = parser.parse_args()

if not os.path.isfile(args.file):
	sys.exit("file {0} doesn't exist".format(args.file))
	
anagrams = collections.defaultdict(list)	
with open(args.file) as words:
	for line in words:
		for word in line.split(' '):
			anagrams[tuple((sorted(filter(lambda a: a != '\n', word))))].append(word.rstrip())
			
for words in anagrams.values():
	for word in words:
		sys.stdout.write(" {0}".format(word))
	sys.stdout.write('\n')

	
			
	


