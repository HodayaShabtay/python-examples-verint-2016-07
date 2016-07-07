import sys

if len(sys.argv) != 3:
	print "Error, expects to receive 2 numbers"
	sys.exit()
	
	
if sys.argv[1].isdigit() == False:
	print "Failure, '", sys.argv[1], "' is not a number, expects to 2 numbers"
	sys.exit()
	
if sys.argv[2].isdigit() == False:
	print "Failure, '", sys.argv[2], "' is not a number, expects to 2 numbers"
	sys.exit()
	
print sys.argv[1] , " + ", sys.argv[2], " = ", int(sys.argv[1])+int(sys.argv[2])