## Assignment 
## Exponent.py
input_base = raw_input("Enter a base: ")
input_exp = raw_input("Enter a exponent: ")
print input_base, "to the power of ", input_exp, " = ", float(input_base)**float(input_exp)


## Sample Example - Functions with return value
def square(number):
    sqr_num = number ** 2
    return sqr_num

input_num = 5
output_num = square(input_num)

print "square of ",input_num, "is ",output_num 

## Sample Example - Documenting functions
def return_difference(n1,n2):
	"""Returns the difference between 2 numbers.
		Subtracts N2 from N1."""
	return n2 - n1