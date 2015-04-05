def factorialDigitSum(n):
	fact = 1
	for i in range (1, n+1):
		fact *= i
	f = str(fact)
	print(f)
	nums = [int(f[x]) for x in range(0, len(f))]
	print(sum(nums))
factorialDigitSum(100)