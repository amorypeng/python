import math
dict = {}
for p in range(1001):
	for a in range(1, int(p/3)):
		if p * (p - 2*a) % (2*p - 2*a) == 0:
			if p not in dict:
				dict[p] = 1
			else:
				dict[p] += 1
print(dict)
print(max(dict, key=dict.get))