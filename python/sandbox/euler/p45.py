def is_pentagonal(num):
	if (1 + (24 * num + 1)**0.5) % 6 > 0:
		return False
	return True

def is_hexagonal(num):
	if (1 + (8 * num + 1)**0.5) % 4 > 0:
		return False
	return True

caught = 0
n = 2
while caught <= 1:
	triangle = n * (n + 1) / 2
	if is_pentagonal(triangle) and is_hexagonal(triangle):
		print(triangle)
		caught += 1
	n += 1