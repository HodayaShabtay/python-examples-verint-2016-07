
from random import randint

sum = 0
numbers = []
for i in range(7):
	numbers.insert(i,randint(1,100))
	sum += numbers[i]
	
print "Sum of numbers:", numbers, "is: ", sum
if sum%7 == 0:
	print "Boom!"