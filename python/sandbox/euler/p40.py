test = '0'
i = 1
while len(test) < 10**6:
	test += str(i)
	i += 1

i = 1
out = 1
while i < 10**6:
	out *= int(test[i])
	i *= 10
print(out)