
import sys
import os

if len(sys.argv) < 3:
	sys.exit("Error, please insert source and destination")
	
if not os.path.isfile(sys.argv[1]) or not os.path.isfile(sys.argv[2]):
	sys.exit("Error, please insert valid source and destination path")

source, dest = sys.argv[1:]
	
with open(source, 'r') as fin:
	with open(dest,'a') as fout:
		for line in fin:
			fout.write("\n {0}".format(line))
	
