import itertools
a=list(itertools.product('AB',range(2)))
print(a)
print('_'*20)
suits='spades hearts diamonds clubs'.split()
a=list(itertools.product('AK',suits))
a=list(itertools.product('ABC',repeat=2))
a=list(itertools.product(range(2),repeat=3))
rows=itertools.product('AB',range(2),repeat=2)
for row in rows:	print(row)
# print(a)