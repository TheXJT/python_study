def chain1(*iterables):
	for it in iterables:
		for i in it:
			yield i

def chain2(*iterables):
	for it in iterables:
		yield from it

s='ABC'
t=tuple(range(3))
print(list(chain2(s,t)))