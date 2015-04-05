import functions
#the function
def d(n):
	list = functions.factor(n)
	list.pop(list.index(n))
	return sum(list)

container = []
#the iterating
for i in range(1, 10000):
	if i == d(d(i)) and i != d(i):
		temp = [i, d(i)]
		temp.sort()
		if temp not in container:
			container.append(temp)

#the sum
sum = 0
for a,b in container:
	sum += a + b
print(sum)