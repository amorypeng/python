import functions
print(functions.factor(28))
print(len(functions.factor(28)))

def triangle(n):
	out = 0
	i = 1
	while len(functions.factor(out)) <= n:
		out += i
		i += 1
	return out
print(triangle(500))