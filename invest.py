## Invest

def invest(amount, rate, time):
	
	print "\n"
	print "Principal Amount: ", amount
	print "Annual Rate of Return: ", rate
	counter=1
	while(counter <= time):
		amount = (amount+(amount*rate))
		print "Year ", counter,": ", amount
		
		counter=counter+1
		

invest(100, .05, 8)
invest(2000, .025, 5)