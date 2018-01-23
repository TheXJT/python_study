from operator import mul
from functools import partial
triple=partial(mul,3)
# print(triple(7))
temp=map(triple,range(1,10))
print(list(temp))