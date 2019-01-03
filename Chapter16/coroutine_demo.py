import inspect

def simple_coroutine():
	print('-> coroutine started')
	x=yield
	print('-> coroutine received:',x)

my_coro=simple_coroutine()
print(my_coro)
# print(inspect.getgeneratorstate(my_coro))

# next(my_coro)
print(inspect.getgeneratorstate(my_coro))
my_coro.send(42)
