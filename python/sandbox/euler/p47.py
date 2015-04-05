import functions
#this is really slow :(
primes_list = functions.primes(10**6)

def prime_factor(n):
	#brute
	out = 0
	i = 0
	while n != 1:
		if n/primes_list[i] % 1 == 0:
			out += 1
			while n/primes_list[i] % 1 == 0:
				n /= primes_list[i]
		i += 1
	return out
	
starting_value = 210 #2*3*5*7, naive check
notFound = True
print(prime_factor(134043))

while(notFound):
	
	if prime_factor(starting_value) != 4:
		starting_value += 1
		continue

	if prime_factor(starting_value + 1) != 4:
		starting_value += 2
		continue
	
	if prime_factor(starting_value + 2) != 4:
		starting_value += 3
		continue
	
	if prime_factor(starting_value + 3) != 4:
		starting_value += 4
		continue
	notFound = False
	print(starting_value)
	