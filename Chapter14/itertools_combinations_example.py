import itertools

a=itertools.combinations('ABCD',2)
a=itertools.combinations_with_replacement('ABCD',2)
a=itertools.count(1,0.5)
# print(list(a))
a=itertools.permutations(range(3))
a=itertools.repeat(10,3)
a=itertools.islice(itertools.count(1,.3),3)
cy=itertools.cycle('ABC')
# print(next(cy))
a=itertools.islice(cy,7)
rp=itertools.repeat(7)
# print(next(rp),next(rp))
a=itertools.repeat(8,4)
import operator
a=map(operator.mul,range(11),itertools.repeat(5))
print(list(a))