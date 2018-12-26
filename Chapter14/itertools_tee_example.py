import itertools
a=itertools.tee('ABC',4)
print(list(zip(*a)))