"""
my_input_file = open("hello.txt", "r")
print ("Line 0 (first line):", my_input_file.readline())

my_input_file.seek(0) # jump back to beginning
print("Line 0 again:", my_input_file.readline())
print("Line 1:", my_input_file.readline())

my_input_file.seek(8) # jump to character at index 8
print("Line 0 (starting at 9th character):", my_input_file.readline())

my_input_file.seek(10, 1) # relative jump forward 10 characters
print("Line 1 (starting at 11th character):", my_input_file.readline())

my_input_file.close()
"""

# Review Exercises

#1
"""
poem_file = open("poetry.py", "r")

line = poem_file.readline()

while line != "":
	print line
	
	line = poem_file.readline()

poem_file.close()


#2
with open("poetry.py", "r") as poetry_file:
	for lines in poetry_file:
		print lines
"""		
#3
## Poetry file in read mode
read_poem = open("poetry.py","r")

## Output file in write mode
write_op = open("output.txt","w")

lines = read_poem.readline()

for line in lines:
	write_op.writelines(line)

read_poem.close()
write_op.close()