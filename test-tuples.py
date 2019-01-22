## Tuples - exercises

# Create a tuple and store strings
cardinal_nums = ("first","second","third")

## Dictionary - exercises

#1 - Empty dictionary 
birthdays = {}

#2 - Add data
birthdays = dict([('Luke Skywalker', '5/24/19'),('Obi-Wan Kenobi', '3/11/57'), ('Darth Vader', '4/1/41')])
print birthdays

#3 Check and add keys
if "Yoda" in birthdays.keys():
	pass
else:
	birthdays["Yoda"] = "unknown"

if "Darth Vader" in birthdays.keys():
	pass
else:
	birthdays["Darth Vader"] = "unknown"

print "\nAfter Adding new values "
print birthdays

#4 - Delete key/value pairs
print
print 'After deleting...  birthdays["Darth Vader"]'

del(birthdays["Darth Vader"])
print birthdays