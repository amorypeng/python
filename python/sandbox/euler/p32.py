check = [str(i) for i in range(1, 10)]

pandigitals = []


for a in range(1, 10000):
	for b in range(a, int(10000/a)):
		test = list(str(a) + str(b) + str(a*b))
		test.sort()
		if test == check:
			if a*b not in pandigitals:
				pandigitals.append(a*b)
				print("got one!", a, b, a*b)
	
	
print(sum(pandigitals))