import functions

#abundant = sum(divisors) > number
#deficient = sum(divisors) < number
#perforect sum(divisors) = number
#all integers >28123 can be written as sum of 2 abundant numbers
#find sum of all positive integers that cannot be written as sum of two abundant numbers

''' Solution:
1. Find all abundant values <= 28123
2. Find list of sum of all combinations
	-trying to store all values gives 10^7 size, faster to create False list and index if True
3. whatever is not in that list of sums is integer that cannot be written as sum of 2 abundant numbers
4. print that sum
'''

#step 1
n = 28124
abundants = []
for i in range(1, n):
	divisors = functions.factor(i)
	divisors.pop(divisors.index(i))
	if sum(divisors) > i:
		abundants.append(i)
#step 2
print(len(abundants))
sums_of_2_abundants = [False for x in range(n)]

for i in range(len(abundants)):
	for j in range(i, len(abundants)):
		temp = abundants[i] + abundants[j]
		if temp < n:
				sums_of_2_abundants[temp] = True
		else: break
print(len(sums_of_2_abundants))

#step 3

out = 0
for i in range(1, n):
	if not sums_of_2_abundants[i]:
		out += i
#step 4
print(out) # ;D
