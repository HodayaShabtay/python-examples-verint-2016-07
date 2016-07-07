
from random import randint

num = randint(1, 1000000)
while num%7 != 0 or num%13 != 0 or num%15 != 0:
	num = randint(1, 1000000)
	
print num