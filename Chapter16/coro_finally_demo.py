class DemoException(Exception):
	pass

def demo_finally():
	print('-> coroutine started')
	try:
		while True:
			try:
				x=yield
			except DemoException:
				print('*** DemoException handled. Continuing...')
			else:
				print('-> coroutine received: {!r}'.format(x))
	finally:
		print('-> coroutine ending')

exc_coro=demo_finally()
next(exc_coro)
exc_coro.send(11)
exc_coro.send(22)
# exc_coro.send(StopIteration)
# exc_coro.close()
# exc_coro.throw(DemoException)
exc_coro.throw(ZeroDivisionError)
# from inspect import getgeneratorstate
# try:
# 	exc_coro.throw(ZeroDivisionError)
# except:
# 	print(getgeneratorstate(exc_coro))
# exc_coro.send(33)
