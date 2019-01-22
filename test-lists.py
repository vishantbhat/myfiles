## Exercises
'''
1. Create a list named desserts that holds the two string values "ice cream" and "cookies"
2. Sort desserts in alphabetical order, then display the contents of the list
3. Display the index number of "ice cream" in the desserts list
4. Copy the contents of the desserts list into a new list object named food
5. Add the strings "broccoli" and "turnips" to the food list
6. Display the contents of both lists to make sure that "broccoli" and "turnips" haven't been added to desserts
7. Remove "cookies" from the food list
8. Display the first two items in the food list by specifying an index range
9. Create a list named breakfast that holds three strings, each with the value of "cookies", by splitting up the string "cookies, cookies, cookies"
10. Define a function that takes a list of numbers, [2, 4, 8, 16, 32, 64], as the argument and then outputs only the numbers from the list that fall between 1 and 20 (inclusive)
'''

## Solutions

#1
desserts = ["ice cream", "cookies"]
print "\n Desserts List"
print desserts

#2
print "\n Sorted Desserts"
desserts.sort()
print desserts

#3
print 
print "Index of Ice Cream: ", desserts.index("ice cream")
  
#4
food = desserts[:]
print
print "Food List after copy"
print food

#5
food.append("broccoli")
food.append("turnips")
print
print "Food List after ading items"
print food

#6
print
print "Food List Contents"
print food

print
print "Desserts List Contents"
print desserts

#7
print 
print "After removing Cookies"
food.remove("cookies")
print food

#8
print
print "First 2 Items of List Food"
print food[0:2]

#9
str_cookies = "cookies, cookies, cookies"
print "\n", str_cookies
breakfast = str_cookies.split(", ")
print "\n After String Split: " , breakfast

#10
def number_subset(num_list):
	return_list = []
	for val in num_list:
		if (val >= 1) and (val <= 20):
			return_list.append(val)
	return return_list
			

list_num = [2, 4, 8, 16, 32, 64]
value = number_subset(list_num)
print "\n", value
