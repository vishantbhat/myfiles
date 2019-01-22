## Simulate Events and Calculate Probabilities - Toss of a coin

from random import randint
'''
# initialise heads nad tails values
heads = 0
tails = 0

# for a 1000 trials of flipping the coin
for i in range(0,1000):
	while randint(0,1) == 0:
		tails +=1
	heads +=1

print "heads = ", heads
print "tails = ", tails
print "heads/tails = ", heads/tails
'''

## Simulate Events and Calculate Probabilities - tossing the die
'''
user_input = int(raw_input("How many times do you want to toss the die? "))

toss = 0
while toss < user_input:
	print "pass ", toss , "cast " , randint(1,6)
	toss +=1
'''
for i in range(0,1000):
	while randint(0,1) == 0:
		tails +=1
	heads +=1

print "heads = ", heads
print "tails = ", tails
print "heads/tails = ", heads/tails