from capitals import capital_dict
import random

# Infinite loop with conditional break
while True:
	
	# Infinite loop for the dictionary
	while capital_dict.keys() != ' ':
		key   = random.choice(capital_dict.keys())
		value = capital_dict[key]		
		
		print "Press space or type 'exit' to quit ... \n"
		print "Question: What is the capital of ", key , "state of US"  
		user_input = raw_input("Answer : ")
		
		if user_input.upper() == value.upper():
			print "\nCorrect"
		else:
			print "\nThe correct answer is", value, ".Goodbye"
			break
	break # Break from outer loop once inner loop is over