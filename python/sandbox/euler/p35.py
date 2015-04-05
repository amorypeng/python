import functions
import itertools
num = 10**6
primes_list = functions.primes(num)
circular_list = []
out = ['0', '2', '4', '6', '8', '5']

for i in primes_list:
	digits = list(str(i))
	check_1 = [var for var in digits if var in out]
	#removes any values with 5 or even
	if (check_1) and len(digits) > 1:
		continue
	else:
		checklist = []
		n = len(digits)
		templist = []
		for i in range(n):
			temp = digits[-i:] + digits[:-i]
			temp = int(''.join(temp))
			#throw away everything if the rotated value is not prime
			if temp not in primes_list:
				templist = []
				break
			else:
				if temp not in templist:
					templist.append(temp)
					
		for obj in templist:
			if obj not in circular_list:
				circular_list.append(obj)

print(len(circular_list))