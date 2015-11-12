#-*- coding: utf-8 -*-
#decorator按照装饰函数是否带参数可以分为2类
#本人理解被装饰函数都带参数，只是参数为不为空的问题
import functools
print('P1-装饰函数不带参数，被装饰函数带参数')
def decorator_one(f1):
    #定义包装函数，用于传递被装饰函数当做参数，使用可变参数和关键字参数可以提升灵活性
    @functools.wraps(f1)
    def wrapper_one(*args, **kw):
        print('start')
        print('call ' + f1.__name__)
        f1(*args, **kw)
        print('end')
       # return f2 *******在函数中使用了被装饰函数，就不用再返回这个函数了，因为已经被执行过了*******
    return wrapper_one

@decorator_one
def f1(s):
    print(s)

#输出两次只为检验装饰器有没有实现"动态增加功能"
f1('test')
print('*****')
f1('test')
print('*****')

print('P2-装饰器函数和被装饰函数都带参数')
#这层传递的参数是装饰函数本身需要使用的参数
def my_decorator_two(*args_decorator,**kw_decorator):
    #这一层函数传递需要被装饰的函数f2
    def decorator_two(f2):
        @functools.wraps(f2)
        #这一层包装函数用于传递被装饰函数f4所需要的参数
        def wrapper_two(*args,**kw):
            print('start')
            print('f2的装饰器函数自带参数为:',*args_decorator)
            print(f2.__name__ + ' is working')
            #在这个函数内已经使用了带参数的被装饰函数f2,所以最后也不需要返回函数f2了
            f2(*args, **kw)
            print('end')
        return wrapper_two
    return decorator_two

@my_decorator_two('my_decorator_four')
def f2(s):
    print(s)

f2('test')
print('*****')
f2('test')
print('*****')

print('P3-习题，设计一个装饰函数带可变参数，被装饰函数不带参数的装饰器')
def my_decorator_three(*args_decorator, **kw_decorator):
    def decorator_three(f3):
        @functools.wraps(f3)
        def wrapper_three(*args,**kw):
            print('begin call')
          #  print(*args,**kw)
            print('f3的装饰器函数自带参数为:',*args_decorator)
            f3(*args,**kw)  # 在函数中使用了被装饰函数，就不用再返回这个函数了，因为已经在这被执行过了
            #print(f3.__name__ + ' is working')
            print('end call')
            #return f3
        return wrapper_three
    return decorator_three

@my_decorator_three()
def f3():
   print('test') 

f3()
print('*****************')
f3()
print('*****************')

@my_decorator_three('execute')
def f4():
    print('test') 

f4()
print('*****************')
f4()
print('*****************')
print('=================')
print(f1.__name__)
print(f2.__name__)
print(f3.__name__)
print(f4.__name__)
