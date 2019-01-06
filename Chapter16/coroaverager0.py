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

from inspect import getgeneratorstate

coro_avg=averager()
print(getgeneratorstate(coro_avg))
next(coro_avg)
print(getgeneratorstate(coro_avg))

coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(5)
print(getgeneratorstate(coro_avg))
