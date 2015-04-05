nums = []
denoms = []
#brute force, probably not very elegant but w/e
for i in range(10, 100):
	for j in range(i+1, 100):
		check_1 = i / j
		check_2 = 1
		trivial = False
		temp_i = list(str(i))
		temp_j = list(str(j))
		temp_i_compare = list(temp_i)
		temp_j_compare = list(temp_j)
		for obj in temp_i:
			if obj in temp_j:
				temp_i.remove(obj)
				temp_j.remove(obj)
				
				if len(temp_i_compare) == 2 and len(temp_j_compare) == 2:
					if temp_i_compare[1] == '0' and temp_j_compare[1] == '0':
						trivial = True
		if len(temp_i) == 1 and len(temp_j) == 1 and not trivial:
			if int(temp_j[0]) != 0:
				check_2 = int(temp_i[0]) / int(temp_j[0])
				
		if check_1 == check_2:	
			print(i, j, check_1, check_2, temp_i,temp_j, trivial)	
			nums.append(i)
			denoms.append(j)
	
out = 1	
for i in denoms:
	out *= i
	
for j in nums:
	out /= j
print(out)
	