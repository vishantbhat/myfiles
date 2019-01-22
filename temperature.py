## Temperature calculation

# Celcius to Farenheit
def celcius_to_farenheit (degree_celcius):
	""" Return thes temperature in Farenheit."""
	return (degree_celcius *(9/5) + 32)


# Farenteit to Celcius
def farenheit_to_celcius(degree_farenheit):
	""" Return the temperature in Farenheit."""
	return ((degree_farenheit-32) * (5/9))

print "32 degree celcius in farenheit ", celcius_to_farenheit(32)
print "32 degree farenheit in celcius ", farenheit_to_celcius(32)