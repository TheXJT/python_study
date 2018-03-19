n=0
for i in range(1,6):
	n ^=i

print(n)
import functools
n=functools.reduce(lambda a,b:a^b,range(6))
print(n)
import operator
n=functools.reduce(operator.xor,range(6))
print(n)