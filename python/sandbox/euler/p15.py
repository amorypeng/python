triangle = [1, 2, 3]
print(triangle[2])

def pascal(n):
	out = []
	out.append([1])
	for i in range(1, n):
		temp = []
		for j in range(i+1):
			if j == 0 or j == i:
				temp.append(1)
			else:
				temp.append(out[i-1][j-1] + out[i-1][j])
		out.append(temp)
	return out
	
print(pascal(20))
