s = 4000000

fib = 1
fibPrev = 1
out = 0

while(fib < s):
	if (fib %2 == 0):
		out += fib
	temp = fib
	fib += fibPrev
	fibPrev = temp

print(out)