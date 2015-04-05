def decorate(func):
	def func_wrap(x, y):
		return func(x, y) + 2
	return func_wrap

@decorate
def add(x, y):
	return x + y
	
print(add(1,2))