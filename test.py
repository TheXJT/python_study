from array import array
import math

class Vector2d:
	__slots__=('__x','__y')
	typecode='d'

	def __init__(self,x,y,z):
		self.__x=float(x)
		self.__y=float(y)
		# self.__z=float(z)

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

v1=Vector2d(3,4,5)
v1._Vector2d__x=float(5)
print(v1.y,v1.x)
print(v1._Vector2d__x)
# v1.__z=2
print(v1.x)