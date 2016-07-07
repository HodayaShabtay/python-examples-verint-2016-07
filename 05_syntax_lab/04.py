

stack = []
print "Enter your string"
input = raw_input()
while input != "":
	stack.insert(len(stack), input)
	input = raw_input()
	
while (len(stack) > 0):
	print stack.pop(), "\n"
