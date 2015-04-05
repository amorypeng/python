import math
high = 20;

def prime(n):
	if n%2 == 0 and n > 2:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True
	
primes = []
for i in range(2, high + 1):
	if prime(i):
		primes.append(i)

prime_dict = {}

for num in primes:
	temp = 1
	while num ** temp < high:
		temp += 1
	prime_dict[num] = temp - 1
	temp = 0

out = 1
print(prime_dict)
for num in prime_dict:
	out *= num ** prime_dict[num]
	
print(out)
	