from array import array
import math

class Vector2d:
	typecode='d'

	def __init__(self,x,y):
		self.__x=float(x)
		self.__y=float(y)

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

v1=Vector2d(3,4)
print(v1.__dict__)
v1._Vector2d__x=float(5)
print(v1.y,v1.x)
print(v1._Vector2d__x)