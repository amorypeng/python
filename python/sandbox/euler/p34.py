factorial = {
	'0' : 1,
	'1' : 1,
	'2' : 2,
	'3' : 6,
	'4' : 24,
	'5' : 120,
	'6' : 720,
	'7' : 5040,
	'8' : 40320,
	'9' : 362880
}

out = 0
#unsure of upper bound
for i in range(3,10**7):
	test = list(str(i))
	check = 0
	for digit in test:
		check += factorial[digit]
	if i == check:
		print(i)
		out += i
print("ans", out)