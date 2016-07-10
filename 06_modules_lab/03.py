"""
This program receives path & size and remove all files are large than the given size recursively
"""


import sys
import operator
import os
from os.path import join, getsize

if len(sys.argv) != 3:
	sys.exit( "Please insert folder path and file size in KB")

if sys.argv[1].isdigit() or not (sys.argv[2].isdigit()):
		sys.exit("Invalid input, please insert valid folder path and file size in KB")
		
path, size = sys.argv[1], operator.mul(int(sys.argv[2]),1024)

try:
	for root,dirs,files in os.walk(path,False):
		for file in files:		
			if getsize(join(root,file)) > size:
				delete = raw_input("The size of {0} is: {1} in bytes are you sure you want to delete it? y/n".format(join(root,file), getsize(join(root,file))))
				if delete == "y":
					os.remove(join(root,file))
					
					
except OSError as exc:
	sys.exit("Exception occurred, close program")
			
	


