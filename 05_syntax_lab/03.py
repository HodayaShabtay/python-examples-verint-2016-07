
from random import randint

sum = 0
num = randint(1,1000)
#print num
while num > 0:
	sum += num%10
	num /= 10	
	
print "Sum=", sum
	