def simple_coro2(a):
	print('-> Started: a=',a)
	b=yield a
	print('-> Received: b=',b)
	c=yield a+b
	print('-> Received: c=',c)

my_coro2=simple_coro2(14)
from inspect import getgeneratorstate
print(getgeneratorstate(my_coro2))
print(next(my_coro2))
print(getgeneratorstate(my_coro2))
print(my_coro2.send(28))
print(getgeneratorstate(my_coro2))

try:
	print(my_coro2.send(99))
except:
	print(getgeneratorstate(my_coro2))