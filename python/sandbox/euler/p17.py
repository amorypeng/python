num_dict = {
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
	100: 'hundred',
	1000: 'thousand'
}

def numToString(n):
	num_str = ''
	if n >= 1000:
		x = n // 1000
		y = 1000
		num_str += num_dict.get(x)
		num_str += num_dict.get(y)
		n -= x * y
	if n >= 100:
		x = n // 100
		y = 100
		num_str += num_dict.get(x)
		num_str += num_dict.get(y)
		
		n -= x*y
		if n != 0:
			num_str += 'and'
	if n >= 20:
		x = n // 10
		y = 10
		num_str += num_dict.get(x* 10)
		n -= x * y
	if n > 0:
		num_str += num_dict.get(n)
	return num_str


def numLetterCount(n):
	out = 0
	for i in range(1, n+1):
		out += len(numToString(i))
	return out
	
print(numToString(342), len(numToString(342)))
print(numToString(115), len(numToString(115)))
print(numLetterCount(1000))
	