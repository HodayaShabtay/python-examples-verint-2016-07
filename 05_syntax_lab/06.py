
from random import randint

first = randint(1,10)
second = randint(1,10)

if first > second:
	big = first
	small = second
else:
	big = second
	small = first

mul = big
while mul%small != 0:
	mul += big
	
print "First number: ", first, " Second number: ", second, " Smallest multiplication: ", mul
	