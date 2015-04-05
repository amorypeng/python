def cyclelength(n):
	rlist = []
	qlist_len = 0
	r = 1
	
	while r:
		r = r % n
		if r in rlist:
			return qlist_len - rlist.index(r)
		rlist.append(r)
		r *= 10
		qlist_len += 1
	return 0

max_len = 0
value = 0
for i in range(2, 1000):
	temp = cyclelength(i)
	if temp > max_len:
		max_len = temp
		value = i
print(max_len, value)
	