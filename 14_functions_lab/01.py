
import sys
from operator import mul
import argparse

def sum_params(*nums):
	return sum([n for n in nums if type(n)==int])
	
	
def mul_params(*nums):
	return reduce(mul,[n for n in nums if type(n)==int])
	

parser = argparse.ArgumentParser(description='This program calculates sum & mul of a given list')
parser.add_argument(nargs='+',help='Insert list of numbers',dest='numbers')
args = parser.parse_args()
	
	
print "Sum of [1,2,3,4, hodaya] is {0}".format(sum_params(args.numbers))
print "Mul of [1,2,3,shabtay,4] is {0}".format(mul_params(args.numbers))
	
	
	
