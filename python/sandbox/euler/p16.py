def powersum(n):
	out = 1
	for i in range(n):
		out *=2
	out_str = list(str(out))
	temp = 0
	for i in range(len(out_str)):
		temp += int(out_str[i])
	out = temp
	return out
	
print(powersum(1000))