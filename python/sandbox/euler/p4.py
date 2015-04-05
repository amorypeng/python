pal = []

for i in range(100, 1000):
	for j in range( 100, 1000):
		s = str(i*j)
		if s[::-1] == s:
			pal.append(int(s))


print(max(pal))