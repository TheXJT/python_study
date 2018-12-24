def vowel(c):
	return c.lower() in 'aeiou'

a=filter(vowel,'Aardvark')

import itertools
a=list(itertools.filterfalse(vowel,'Aardvark'))
a=list(itertools.dropwhile(vowel,'Asardvark'))
a=list(itertools.takewhile(vowel,'Aardvark'))
a=list(itertools.compress('Aardvark',(1,0,1,1,0,1)))
a=list(itertools.islice('Aardvark',1,7,2))
print(list(a))