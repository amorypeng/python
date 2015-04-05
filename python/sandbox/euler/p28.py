nums = []
nums.append(1)

value = 1

for i in range(1,501):
	for j in range(1, 5):
		value +=  2 * i
		nums.append(value)
print(sum(nums))