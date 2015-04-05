#non recursive
def fibo(n):
	if n <= 1:
		return n
	else:
		fib = 1
		fibPrev = 1
		for i in range(2, n):
			temp = fib
			fib += fibPrev
			fibPrev = temp
	return fib
	
i = 0
while len(str(fibo(i))) < 1000:
	i += 1
	
print(i, fibo(i))
