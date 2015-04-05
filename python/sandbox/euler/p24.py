'''
thxs python
'''
import itertools

test = [x for x in range(10)]
print(list(itertools.permutations(test, 10))[999999])