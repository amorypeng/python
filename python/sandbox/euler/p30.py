n = 5

out = []
for i in range(2, 999999):
	test = []
	check = i
	while (i / 10 != 0):
		test.append(i % 10)
		i //= 10
	temp = 0
	for j in test:
		temp += j**n
	if temp == check:
		out.append(temp)
print(out, sum(out))
		