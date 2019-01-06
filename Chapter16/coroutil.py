from functools import wraps

def coroutine(func):
	@wraps(func)
	def primer(*args,**kwargs):
		gen=func(*args,**kwargs)
		next(gen)
		return gen
	return primer

@coroutine
def averager():
	total=0.0
	count=0
	average=None
	while True:
		print(average)
		term=yield average
		total+=term
		count+=1
		average=total/count

coro_avg=averager()
from inspect import getgeneratorstate
print(getgeneratorstate(coro_avg))
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(5)