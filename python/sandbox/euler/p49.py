#p49

import functions

primes_list = functions.primes(9999)
primes_table = [False]*99999 #values after 9999 are irrelevant
for prime in primes_list:
	primes_table[prime] = True
	
def is_perm(i, j):
	check_i = list(str(i))
	check_i.sort()
	check_j = list(str(j))
	check_j.sort()
	if check_i == check_j:
		return True
	return False
	


out = []
found = 0
for i in primes_list:
	for test in range(primes_list.index(i)):
		j = primes_list[test]
		difference = i - j
		
		if primes_table[i + difference]:
			if is_perm(i, j) and is_perm(i, i+difference):
				out.append(i)
				out.append(j)
				out.append(i+difference)
				found += 1
				print(out)
	if found == 2:
		break
print(out)