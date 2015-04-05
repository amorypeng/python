import functions

primeslist = functions.primes(100000)
isprime = [False] * 100000
for i in primeslist:
	isprime[i] = True
	
max_a = 0
max_b = 0
prime_count = 0

for a in range(-999, 1000):
	for b in range(-999, 1000):
		n = 0
		while isprime[abs(n*n + n*a + b)]:
			n += 1
		if n > prime_count:
			prime_count = n
			max_a = a
			max_b = b

print(max_a, max_b, prime_count, max_a * max_b)