f = open("p13.txt", 'r')
num = []
s = f.readline()
while(s):
	num.append(int(s))
	s = f.readline()

print(len(num))
print(sum(num))