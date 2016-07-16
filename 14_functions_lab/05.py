
import sys
import os
import collections

def groupby(f, *mylist):
	dic = collections.defaultdict(list)
	try:
		for n in mylist:
			dic[f(n)].append(n)
		return dic
	except:
		print "{0}, {1}".format(sys.exc_info()[0],sys.exc_info()[1])
		
print groupby(lambda s: s[0], 'hello', 'hi', 'help', 'bye', 'hodaya')