import itertools

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

count = 0

def subdivide(test):
	if int(test[1:4]) % 2 != 0:
		return False
	elif int(test[2:5]) % 3 != 0:
		return False
	elif int(test[3:6]) % 5 != 0:
		return False
	elif int(test[4:7]) % 7 != 0:
		return False
	elif int(test[5:8]) % 11 != 0:
		return False
	elif int(test[6:9]) % 13 != 0:
		return False
	elif int(test[7:10]) % 17 != 0:
		return False
	else:
		return True

print(subdivide('1406357289'))
for perm in itertools.permutations(nums, len(nums)):
	test = ''.join(list(perm))
	if int(test) >= 10**9:
		if subdivide(test):
			print(test)
			count += int(test)
		
print(count)
