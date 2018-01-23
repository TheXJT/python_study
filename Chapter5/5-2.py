def factorial(n):
	'''returns n!'''
	return 1 if n<2 else n*factorial(n-1)

# fact=factorial
# print(fact(5))
# temp=map(factorial,range(11))
# print(list(temp))
# print([fact(n) for n in range(11)])
# temp2=map(factorial,filter(lambda n: n % 2,range(6)))
# print(list(temp2))
# print(factorial(n) for n in range(6) if n%2)
print(dir(factorial))