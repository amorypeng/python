import functions
prime_list = functions.primes(10**6)

prime_table = [False] * 10**6

for prime in prime_list:
	prime_table[prime] = [True]
	
conjecture = True
test = 7

while conjecture:
	if prime_table[test]:
		test += 2
	
	conjecture = False
	i = 0
	while prime_list[i] < test:
		if ((test - prime_list[i])/2)**0.5 % 1 == 0:
			print(test)
			test += 2
			conjecture = True
			break
		i += 1
print(test)