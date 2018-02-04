from functools import singledispatch

@singledispatch
def test(obj):
	return obj.__doc__
	# pass

@test.register(str)
def _(text):
	print('This is str')

@test.register(int)
def _(n):
	print('that is int')

print(test(4))