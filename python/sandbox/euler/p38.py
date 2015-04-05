def ispandigital(num):
	check = ''
	n = 1
	while len(check) < 9:
		check += str(n * num)
		n += 1
	#print(check)
	check_list = list(check)
	check_list.sort()
	#print(check_list)
	if check_list == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		return (check, True)
	else:
		return (check, False)
	
for i in range(10**5):
	value, test = ispandigital(i)
	if test: print(value, i)
