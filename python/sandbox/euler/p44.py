import math

def is_pentagonal(num):
	if (1 + (24 * num + 1)**0.5) % 6 > 0:
		return False
	return True

n = 1
not_caught = True
while not_caught:
	n += 1
	j = n*(3*n-1)/2
	for i in range(n-1, 1, -1):
		k = i*(3*i-1)/2
		if is_pentagonal(j+k) and is_pentagonal(abs(j-k)):
			print(i, n, abs(j-k))
			not_caught = False
			break
	