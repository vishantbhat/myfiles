## List of Lists

def enrollment_stats(list_stud):
	
	'''This function, takes, as an input, a list of lists where each individual list contains three elements: 
     (a) the name of a university, 
     (b) the total number of enrolled students, and 
     (c) the annual tuition fees.
	 This function should return two lists: the first containing all of the student enrollment values and
	 the second containing all of the tuition fees.'''
	
	# Lists to store student enrollment and fees records
	list_stud_enrol = []
	list_stud_fees = []
		
	for values in list_stud:
		list_stud_enrol.append(values[:][1])
		list_stud_fees.append(values[:][2])
		
	# Return lisis
	return list_stud_enrol, list_stud_fees

def student_stats(list_stud_values):

	sum_val = 0
	med_val = 0
	men_val = 0
	temp_list = []
	temp_list.extend(list_stud_values)
	
	# Sort the list first
	temp_list.sort()
	
	# Sum of all values
	for values in temp_list:
		sum_val += values
	
	# Mean of all values
	men_val = sum_val / len(temp_list)
	
	## Calculate Median ##
	
	# Index of the median value - check for odd or even length 
	if (len(temp_list)%2) == 0:
		med_val_indx = (len(temp_list)/2) + 1
	else:
		med_val_indx = (len(temp_list) + 1)/2
	
	# Median value
	med_val = temp_list[med_val_indx]
	
	return sum_val, men_val, med_val
	

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

stud_enrol, stud_fees = enrollment_stats(universities)

print "\n Enrollment ..."
print stud_enrol

print "\n Fees ..."
print stud_fees

# Function call to collect statistics
tot_stud, mean_stud, median_stud = student_stats(stud_enrol)
tot_tuit, mean_tuit, median_tuit = student_stats(stud_fees)

# Display Statistics
print
print "*"*25
print "Total Students: ", tot_stud
print "Total Tuition: ", tot_tuit
print
print "Student Mean: ", mean_stud
print "Student Median: ", median_stud
print
print "Tuition Mean: ", mean_tuit
print "Tuition Median: ", median_tuit
print "*"*25