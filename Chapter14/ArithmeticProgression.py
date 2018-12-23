class ArithmeticProgression:

	def __init__(self,begin,step,end=None): #1
		self.begin=begin
		self.step=step
		self.end=end

	def __iter__(self):
		result=type(self.begin+self.step)(self.begin) #2
		forever=self.end is None #3
		index=0
		while forever or result < self.end: #4
			yield result #5
			index +=1
			result=self.begin+self.step*index #6

ap=ArithmeticProgression(0,1,3)
print(list(ap))
ap=ArithmeticProgression(1,.5,3)
print(list(ap))
ap=ArithmeticProgression(0,1/3,1)
print(list(ap))
from fractions import Fraction
ap=ArithmeticProgression(0,Fraction(1,3),1)
print(list(ap))
# print(type(0+Fraction(1/3)))
from decimal import Decimal
ap=ArithmeticProgression(0,Decimal('.1'),.3)
print(list(ap))
# print(Decimal('.1'))