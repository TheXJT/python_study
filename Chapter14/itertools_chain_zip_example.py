import itertools
a=list(itertools.chain('ABC',range(2)))
a=list(itertools.chain(enumerate('ABC')))
a=list(itertools.chain.from_iterable(enumerate('ABC')))
a=list(zip('ABC',range(5)))
a=list(zip('ABC',range(5),[10,20,30,40]))
a=list(itertools.zip_longest('ABC',range(5)))
a=list(itertools.zip_longest('ABC',range(5),fillvalue='?'))
print(a)