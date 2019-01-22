## Assignment - find all of the integers that divide evenly into an integer provided by the user.

# Function to check the divsor of the number
def find_divisor(number):
	''' This function prints all the divisors of the given positive integer.'''
	# Check factors of the integer
	if (number <= 0):
		print "Entered value is not a positive integer"
	elif (number > 0):
		for counter in range (1,number+1):
			if (number % counter) >0 :
				pass
			else:
				print counter, "is a divisor of ",number

# User Input
input_integer = int(raw_input("Enter a positive integer: "))

find_divisor(input_integer)