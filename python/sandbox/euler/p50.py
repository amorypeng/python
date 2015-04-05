#p50

import functions

n = 10**6
primes_list = functions.primes(n)
sum_of_primes = list(primes_list)
num_of_primes = 0

primes_table = [False] * 10**8
for prime in primes_list:
	primes_table[prime] = True
	
for i in range(1, len(sum_of_primes)):
	sum_of_primes[i] += sum_of_primes[i-1]

terms = 0
value = 0
for i in range(num_of_primes, len(primes_list)):
	for j in range(i - num_of_primes - 1, -1, -1):
		if sum_of_primes[i] - sum_of_primes[j] > n:
			break
		if primes_table[sum_of_primes[i] - sum_of_primes[j]]:
			if i - j > terms:
				terms = i - j
				num_of_primes = terms
				value = sum_of_primes[i] - sum_of_primes[j]
				print(terms, value)
print(terms, value)