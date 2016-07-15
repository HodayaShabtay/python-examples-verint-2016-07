
import sys
import os
import argparse

def except_for_string_int(val1, val2):
	try:
		if val1.isdigit():
			if val2.isdigit():
				raise ValueError('excepts for integer and string, received tow integers')
			else:
				print "Valid input"
		elif not val2.isdigit():
			raise ValueError('excepts for integer and string, received two strings')
		else:
			print "Valid input"
	except ValueError as ex:
		print "{0}, {1}".format(type(ex), ex.args)	
		
		
parser = argparse.ArgumentParser(description='This program excepts for integer and string')
parser.add_argument(help='Integer',dest='val1')
parser.add_argument(help='String',dest='val2')
args = parser.parse_args()

except_for_string_int(args.val1,args.val2)

