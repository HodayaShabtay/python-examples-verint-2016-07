
import sys
import os

def length_validation(length, *words):
	try:
		return list(word for word in words if len(word)>length)
	except:
		print "{0}, {1}".format(sys.exc_info()[0],sys.exc_info()[1])
	
	
print length_validation(3, 'dad', 'book','child','pen')
print length_validation(3, 'dad', 'book','child','pen',3333)
