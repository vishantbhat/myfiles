## Assignment - Wax Poerty
import random

def rand_choice(list,limit):
	subset_list = []

	while True:
		rand_val = random.choice(list)
		if rand_val not in subset_list:
			subset_list.append(rand_val)
		
		if len(subset_list) > (limit-1):
			break
	return subset_list
	
def makePoem():
	nouns        = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
	verbs        = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
	adjectives   = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
	prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
	adverbs      = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
	
	# Select 3 unique random nouns
	unique_nouns = []
	unique_nouns = rand_choice(nouns,3)
	print unique_nouns

	# Select 3 unique random verbs
	unique_verbs = []
	unique_verbs = rand_choice(verbs,3)
	print unique_verbs	

	# Select 3 unique random adjectives
	unique_adj = []
	unique_adj = rand_choice(adjectives,3)
	print unique_adj

	# Select 1 unique random adverb
	unique_adverb = random.choice(adverbs)
	print unique_adverb

	# Select 2 unique random prepositions
	unique_prep = []
	unique_prep = rand_choice(prepositions,2)
	print unique_prep
	
	# the "A" in the title and the first line is adjusted to become an "An" automatically if the first adjective begins with a vowel
	if ((unique_adj[0][0].find("a") > 0)
	   or (unique_adj[0][0].find("e") > 0) 
	   or (unique_adj[0][0].find("i") > 0)
	   or (unique_adj[0][0].find("o") > 0)
	   or (unique_adj[0][0].find("u") > 0)):
		begin_sentence = "An"
	else:
		begin_sentence = "A"
	
	## My Poem
	print
	print "{} {} {}".format(begin_sentence,unique_adj[0],unique_nouns[0])
	print "-"*25
	print
	print "{} {} {} {} {} the {} {}".format(begin_sentence,unique_adj[0],unique_nouns[0],unique_verbs[0],unique_prep[0],unique_adj[1],unique_nouns[1])
	print "{}, the {} {}".format(unique_adverb,unique_nouns[0],unique_verbs[0])
	print "the {} {} {} a {} {}".format(unique_nouns[1],unique_verbs[2],unique_prep[1],unique_adj[2],unique_nouns[2])
	
makePoem()