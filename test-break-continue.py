## Sample Script to check for a specific alphabet
"""
phrase = "it marks the spot"

for letter in phrase:
    if letter == "X":
        break
else:
    print("There was no 'X' in the phrase")
"""

## Sample Script to get password
"""
tries = 0

while tries < 3:
    password = raw_input("Password: ")
    if password == "I<3Bieber":
        break
    else:
        tries = tries + 1
else:
    print("Suspicious activity. The authorities have been alerted.")
"""

## Sample script to quit on accepting Q/q
"""
while True:
	user_input = raw_input("Enter a string (enter Q/q to quit): ")
	if user_input == 'Q' or user_input == 'q':
		break
"""

## Sample script to print all numbers between 1-50 which are not a multiple of 3
"""
for num in range(1,51):
	if num % 3 == 0:
		continue
	else:
		print num, "is NOT a multiple of 3"
"""

## Script for TRY/EXCEPT scenario
"""
try:
    number = int(raw_input("Enter an integer: "))
except ValueError:
    print ("That was not an integer.")
"""

## Rewiew Exercise: Script to catch ValueError repeatedly and display number if entered
while True:
	try:
		user_input = int(raw_input("Enter an integer: "))
		print user_input, "is the entered value"
		break
	except ValueError:
		print "Try Again.."