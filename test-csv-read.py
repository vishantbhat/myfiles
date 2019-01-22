# test CSV reading
import os
import csv

"""
base_path = "C:\myprojects"

with open(os.path.join(base_path,"wonka.csv"),"r") as my_file:
	my_file_reader = csv.reader(my_file)
	
	for row in my_file_reader:
		print row



base_path = "C:\myprojects"

with open(os.path.join(base_path,"wonka.csv"), "r") as my_file:
	my_file_reader = csv.reader(my_file)
	
	next(my_file_reader)
	
	for firstname,lastname,reward in my_file_reader:
		print "{} {} got: {}".format(firstname, lastname, reward)


		
base_path = "C:\myprojects"

with open(os.path.join(base_path,"tabbed_wonka.csv"), "r") as my_file:
	my_file_reader = csv.reader(my_file, delimiter="\t")
	
	next(my_file_reader)
	
	for row in my_file_reader:
		print row
		


base_path = "C:\myprojects"

with open(os.path.join(base_path, "movies.csv"), "w") as my_file:
    my_file_writer = csv.writer(my_file)
    my_file_writer.writerow(["Movie", "Rating"])
    my_file_writer.writerow(["Rebel Without a Cause", "3"])
    my_file_writer.writerow(["Monty Python's Life of Brian", "5"])
    my_file_writer.writerow(["Santa Claus Conquers the Martians", "0"])

"""
my_path = "C:\myprojects"

my_ratings = [ ["Movie", "Rating"],
              ["Rebel Without a Cause", "3"],
              ["Monty Python's Life of Brian", "5"],
              ["Santa Claus Conquers the Martians", "0"] ]

with open(os.path.join(my_path, "movies.csv"), "w") as my_file:
    my_file_writer = csv.writer(my_file)
    my_file_writer.writerows(my_ratings)
