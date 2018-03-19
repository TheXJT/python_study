from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools

class Vector:
	# __slots__=('__x','__y')
	typecode='d'

	def __init__(self,components):
		self._components=array(self.typecode,components)

	def __iter__(self):
		return iter(self._components)

	def __repr__(self):
		components=reprlib.repr(self._components)
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
		cls=type(self)
		if isinstance(index,slice):
			return cls(self._components[index])
		elif isinstance(index,numbers.Integral):
			return self._components[index]
		else:
			msg='{cls.__name__} indices must be integers'
			raise TypeError(msg.format(cls=cls))

	shortcut_names='xyzt'

	def __getattr__(self,name):
		cls=type(self)

		if len(name)==1:
			pos=cls.shortcut_names.find(name)
			if 0<=pos<len(self._components):
				return self._components[pos]
		msg='{.__name__!r} object has no attribute {!r}'
		raise AttributeError(msg.format(cls,name))

	def angle(self,n):
		r=math.sqrt(sum(x*x for x in self[n:]))
		a=math.atan2(r,self[n-1])
		if (n==len(self)-1) and (self[-1]<0):
			return math.pi*2-a
		else:
			return a

	def angles(self):
		return (self.angle(n) for n in range(1,len(self)))

	def __format__(self,fmt_spac=''):
		if fmt_spac.endswith('h'):
			fmt_spac=fmt_spac[:-1]
			coords=itertools.chain([abs(self)],
				self.angles())
			outer_fmt='<{}>'
		else:
			coords=self
			outer_fmt='({})'
		components=(format(c,fmt_spac) for c in coords)
		return outer_fmt.format(', '.join(components))

	@classmethod
	def frombytes(cls,octets):
		typecode=chr(octets[0])
		memv=memoryview(octets[1:]).cast(typecode)
		return cls(memv)


s=Vector([-1,-1,-1,-1])
print(format(s,'.5fh'))

my_list=[[1,2,3],[40,50,60],[9,8,7]]
import functools
s=functools.reduce(lambda a,b:a+b[1],my_list,0)

print(s)
import numpy as np
my_array=np.array(my_list)
print(np.sum(my_array[:,1]))
print(functools.reduce(operator.add,[sub[1] for sub in my_list],0))
s=sum(sub[1] for sub in my_list)
print(s)