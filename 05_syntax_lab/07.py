
from random import randint

num = randint(1,100)
print "Insert Your Guesswork"

input = int(raw_input())
while input != num:
	if input > num:
		print "Too Big :("
	else:
		print "Too Small :("
	input = int(raw_input())
print "Bingo!! :)"
	