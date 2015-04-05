def ispalindrome(s):
	if s == s[::-1]:
		return True

print(bin(585)[3:])
out = 0
for i in range(10**6):
	if ispalindrome(str(i)) and ispalindrome(str(bin(i))[2:]):
		print(i, bin(i))
		out += i
print(out)