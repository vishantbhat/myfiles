## Check character length of entered string

# User Input
user_input = raw_input ("Enter a string: ")

if len(user_input) == 5:
	print "Length of string is equal to 5 characters"
elif len(user_input) < 5:
	print "Length of string is less than 5 characters"
else:
	print "Length of string is greater than 5 characters"