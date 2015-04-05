from math import sqrt

def isprime(n):
	if n == 2: return True
	if n < 2 or n%2 == 0: return False
	for i in range(3, int(sqrt(n)) + 1, 2):
		if n % i == 0: return False
	return True
	
r = 10001

primes = []
i = 2
while len(primes) < r:
	if isprime(i): primes.append(i)
	i += 1

print(primes)