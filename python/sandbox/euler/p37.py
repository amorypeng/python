import functions

primes_list = functions.primes(10**6)
primes_table = [False] * 10**6
for prime in primes_list:
	primes_table[prime] = True
	

def truncatable(n):
	right = n
	left = n
	while right:
		right //= 10
		if right == 0:
			break
		#print(right)
		if not primes_table[right]:
			return False
	while left:
		left = int(str(left)[1:])
		#print(left)
		if not primes_table[left]:
			return False
		if len(str(left)) == 1:
			break
	return True
	
count = 0
iter = 4 #start at 11
sum = 0
while count != 11:
	if truncatable(primes_list[iter]):
		count += 1
		print(primes_list[iter])
		sum += primes_list[iter]
	iter += 1
print(sum)