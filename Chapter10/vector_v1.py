from array import array
import reprlib
import math
import functools
import operator

class Vector:
	# __slots__=('__x','__y')
	typecode='d'

	def __init__(self,components):
		self._components=array(self.typecode,components)

	def __iter__(self):
		return iter(self._components)

	def __repr__(self):
		components=reprlib.repr(self._components)
		print(components)
		# print(self._components)
		components=components[components.find('['):-1]
		return 'Vector({})'.format(components)

	def __str__(self):
		return str(tuple(self))


	def __bytes__(self):
		return (bytes([ord(self.typecode)])+
			bytes(self._components))

	def __eq__(self,other):
		# return tuple(self)==tuple(other)
		# if len(self)!=len(other):
		# 	return False
		# for a,b in zip(self,other):
		# 	if a!=b:
		# 		return False
		# return True
		return len(self)==len(other) and all(a==b for a,b in zip(self,other))

	def __hash__(self):
		# hashes=(hash(x) for x in self._components)
		hashes=map(hash,self._components)
		return functools.reduce(operator.xor,hashes,0)

	def __abs__(self):
		return math.sqrt(sum(x*x for x in self))

	def __bool__(self):
		return bool(abs(self))

	def __len__(self):
		return len(self._components)

	def __getitem__(self,index):
		return self._components[index]

	@classmethod
	def frombytes(cls,octets):
		typecode=chr(octets[0])
		memv=memoryview(octets[1:]).cast(typecode)
		return cls(memv)


s=Vector(range(10000))
print(hash(s))
print(s==range(10000))
# print(hash(Vector((1,2,3))))
s=zip(range(3),'ABC',[0.0,1.1,2.2,3.3])
# print(s)
print(list(s))
from itertools import zip_longest
s1=zip_longest(range(3),'ABC',[0.0,1.1,2.2,3.3],fillvalue=-1)
print(list(s1))