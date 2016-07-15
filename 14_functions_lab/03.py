
import sys
import os

def calculate(*nums):
	try:
		return sum([n%100/10 for n in nums])
	except:
		print "{0}, {1}".format(sys.exc_info()[0],sys.exc_info()[1])
	
	
print calculate(1120, 220, 140)
print calculate('hodaya', 400,800)
print calculate(900, 400,800)