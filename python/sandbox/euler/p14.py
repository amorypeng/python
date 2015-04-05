def collatz(n):
	out = []
	out.append(int(n))
	while n != 1:
		if n%2 == 0:
			n /= 2
		elif n%2 != 0:
			n = 3*n + 1
		out.append(int(n))
	return out
	
max_collatz = 0
max_collatz_value = 1

for i in range(1, 1000000):
	if len(collatz(i)) > max_collatz:
		max_collatz = len(collatz(i))
		max_collatz_value = i


print(max_collatz_value)