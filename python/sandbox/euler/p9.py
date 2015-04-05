import math

for i in range(1, 1000):
	for j in range(i, 1000):
		k = int(math.sqrt(i**2 + j**2))
		if math.sqrt(i**2 + j**2) == k:
			if i + j + k == 1000:
				print(i, j, k, i*j*k)
			