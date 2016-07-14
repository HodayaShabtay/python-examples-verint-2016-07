
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='This program retrive IP for hostname')
parser.add_argument(help='IP addresses file',dest='file')
parser.add_argument(nargs='+',help='hostnames list',dest='hosts')

args = parser.parse_args()

if not os.path.isfile(args.file):
	sys.exit("error! file {0} doesn't exist".format(args.file))

dic = {}
with open(args.file) as file:
	for line in file:
		dic[line.split('=')[0]] = line.split('=')[1]

for item in args.hosts:
	if item in dic:
		print dic[item]
	else:
		print "hostname '{0}' was not found".format(item)
		




