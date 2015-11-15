#-*- coding: utf-8 -*-
import functools
from types import MethodType

class Student(object):
    __slots__=('name','sex','math_score','history_score')
    
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    
    def start_speak(self,stu):
        stu.speak()

def speak(self,s='Nothing to say!'):
    print('Start to say something:')
    print(s)

class Chinese_stu(Student):
    def speak(self,s='Nothing to say'):
        print('Start to say chinese:')
        print(s)

class English_stu(Student):
    def speak(self,s='Nothing to say'):
        print('Start to say English:')
        print(s)

class Japanese_stu(Student):
    def speak(self,s='Nothing to say'):
        print('Start to say japanese:')
        print(s)

#使用__slot__和types.MethodType()函数
stu=Student('kami','男')
print(stu.name)
stu.math_score=70
stu.history_score=80
#stu.chinese_score=100  这一句无法执行，因为没有chinese_score这个属性
#这里增加的是类的函数而不是实例的函数，需要注意
Student.speak=MethodType(speak,Student)
stu.speak('Hello World')

#使用子类来构建偏函数
chinese_stu=Chinese_stu('小凯','男')
print(chinese_stu.name)
chinese_stu.speak('我热爱python!')
say_hello=functools.partial(chinese_stu.speak,'您好，偏函数')
say_hello()

#应用类的多态特性

#生成日本和英国学生实例
japanese_stu=Japanese_stu('安倍晋三','不明')
english_stu=English_stu('Jack','man')

stu.start_speak(stu)
stu.start_speak(chinese_stu)
stu.start_speak(japanese_stu)
stu.start_speak(english_stu)
