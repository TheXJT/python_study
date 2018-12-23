import itertools

def aritprog_gen(begin,step,end=None):
	first=type(begin+step)(begin)
	ap_gen=itertools.count(first,step)
	if end is not None:
		ap_gen=itertools.takewhile(lambda n: n<end,ap_gen)
	return ap_gen

ap=aritprog_gen(0,1,3)
print(list(ap))
ap=aritprog_gen(1,.5,3)
print(list(ap))
ap=aritprog_gen(0,1/3,1)
print(list(ap))
from fractions import Fraction
ap=aritprog_gen(0,Fraction(1,3),1)
print(list(ap))
# print(type(0+Fraction(1/3)))
from decimal import Decimal
ap=aritprog_gen(0,Decimal('.1'),.3)
print(list(ap))
# print(Decimal('.1'))