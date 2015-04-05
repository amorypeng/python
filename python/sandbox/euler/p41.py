import functions
import itertools

def pandigital_prime(checklist):
	for perm in itertools.permutations(checklist, len(checklist)):
		if functions.is_prime(int(''.join(perm))):
			print(''.join(perm))

checklist = []
for i in range(1, 10):
	checklist.append(str(i))
	pandigital_prime(checklist)