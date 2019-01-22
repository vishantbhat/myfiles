## Cats with Hats

# 100 cats with hats ON

cats = {}

for i in range(1, 101):
  cats['cat' + str(i)] = "OFF"


for round in range(1, 101):
	for cat in range(1, 101):
		if cat % round == 0:
			if cats['cat' + str(cat)] == "OFF":
				cats['cat' + str(cat)] = "ON"
			else:
				cats['cat' + str(cat)] = "OFF"

for c, hats in cats.items():
	if cats[c] == "ON":
		print(c + ' has a hat.')