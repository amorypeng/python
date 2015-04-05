n = 100

s = set()
for a in range(2, n+1):
	for b in range(2, n+1):
		if a**b not in s:
			s.add(a**b)
print(len(s))