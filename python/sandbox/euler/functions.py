import math
def primes(n):
    """ Returns  a list of primes < n """ #thxs stackoverflow 
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
	
def factor(n):
	"""returns list of factors"""
	out = []
	for i in range(1, 1+int(math.sqrt(n))):
		if (n%i) == 0: 
			out.append(int(i))
			#check for square
			if int(n/i) != int(i):
				out.append(int(n/i))
	return out

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
	
def prime_factor(n):
	#brute
	primes_list = primes(n)
	out = []
	i = 0
	while n != 1:
		while n/primes_list[i] % 1 == 0:
			n /= primes_list[i]
			out.append(primes_list[i])
		i += 1
	return out