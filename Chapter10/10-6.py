# BEGIN VECTOR_V1
from array import array
import reprlib
import math
import numbers


class Vector:
    typecode = 'd'
    shortcut_names='xyzt'

    def __init__(self, components):
        self._components = array(self.typecode, components)  # <1>

    def __iter__(self):
        return iter(self._components)  # <2>

    def __repr__(self):
        components = reprlib.repr(self._components)  # <3>
        components = components[components.find('['):-1]  # <4>
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))  # <5>

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))  # <6>

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

    def __getattr__(self,name):
        cls=type(self)

        if len(name)==1:
            pos=cls.shortcut_names.find(name)
            if 0<=pos<len(self._components):
                return self._components[pos]
        msg='{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls,name))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)  # <7>
# END VECTOR_V1

v1=Vector(range(7))
print(v1)
s=v1[-1:]
print(type(s))
print(s)
s2=v1[1,2]