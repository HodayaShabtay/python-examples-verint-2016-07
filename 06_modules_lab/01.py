
import sys

if len(sys.argv) < 2:
	print "Error, please send number as argument"
	sys.exit()
	
if sys.argv[1].isdigit() == False:
	print "Strings are not valid as argument, only numbers"
	sys.exit()
	
for i in range(int(sys.argv[1])):
	print "Hello\n"
	