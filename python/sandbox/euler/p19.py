#doomsday
#month = [non-leap leap(if available)]
dooms_dict = {
	'Jan' : [3, 4],
	'Feb' : [28, 29],
	'Mar' : [14, 14],
	'Apr' : [4, 4],
	'May' : [9, 9],
	'Jun' : [6, 6],
	'Jul' : [11, 11],
	'Aug' : [8, 8],
	'Sep' : [5, 5],
	'Oct' : [10, 10],
	'Nov' : [7, 7],
	'Dec' : [12, 12]
}

week = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

def findDoomsday(year):
	cycle_check = int((year/100)%4)
	if cycle_check == 0:
		index = 2
	elif cycle_check == 1:
		index = 0
	elif cycle_check == 2:
		index = 5
	elif cycle_check == 3:
		index = 3
	
	num = int(str(year)[-2:])
	q = int(num / 12)
	r = num % 12
	s = int(r / 4)
	value = q + r + s
	out = week[(value + index)%7]
	return out

def calcDay(day, month, year):
	#find the doomsday
	doomsday = findDoomsday(year)
	doomsdate = 0
	target = ""
	#calculate what date the doomsday is (leap or not leap)
	leap = False
	if year%4==0 and (year%400 == 0 or year%100 != 0):
		leap = True
	if leap:
		doomsdate = dooms_dict.get(month)[1]
	else:
		doomsdate = dooms_dict.get(month)[0]
		
	#find the difference between the day and the doomsdate
	if day < doomsdate:
		diff = (doomsdate - day)%7
		target = week[(week.index(doomsday) - diff)%7]
	elif day >= doomsdate:
		diff = (day - doomsdate)%7
		target = week[(week.index(doomsday) + diff)%7]
	print(target, doomsday, doomsdate)
	return target

calcDay(4, 'Jul', 1776)

#solving the problem (finally)
answer = 0
for year in range(1901, 2001):
	for key in dooms_dict:
		if calcDay(1, key, year) == 'Sun': answer += 1
print(answer)