def primes(n):
	factors = []
	d = 2
	while n > 1:
		while n%d == 0:
			factors.append(d)
			n = n/d
		d = d + 1
		if d*d > n:
			if n > 1: 
				factors.append(n)
				break
	return factors
	
pf = primes(600851475143)
print(max(pf))
			