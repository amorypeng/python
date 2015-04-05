f = open('p11-grid.txt', 'r')

nums = []
s = f.readline()
while(s):
	row_temp = s.split()
	row = [int(i) for i in row_temp]
	nums.append(row)
	s = f.readline()

#len(array) gets rows
#len(array[i]) gets columns
#and so on for multiple dimensions
print(nums)
products = []
for i in range(0, len(nums)-4):
	for j in range(0, len(nums[i]) -4):
		mult_right = nums[i][j] * nums[i][j+1] * nums[i][j+2] * nums[i][j+3]
		mult_down = nums[i][j] * nums[i+1][j] * nums[i+2][j] * nums[i+3][j]
		mult_diagdown = nums[i][j] * nums[i+1][j+1] * nums[i+2][j+2] * nums[i+3][j+3]
		if j > 2:
			mult_diagup = nums[i][j] * nums[i+1][j-1] * nums[i+2][j-2] * nums[i+3][j-3]
			products.append(mult_diagup)
		products.append(mult_right)
		products.append(mult_down)
		products.append(mult_diagdown)

print(max(products))
