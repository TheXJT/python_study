#-*- coding: utf-8 -*-
#decorator按照装饰函数和被装饰函数是否带参数可以分为4类
import functools
print('P1-两者都不带参数')
def decorator_one(f1):
    @functools.wraps(f1)
    def wrapper_two(*args, **kw):
        print('start')
        print('call ' + f1.__name__)
        print('end')
        return f1
    return wrapper_two

@decorator_one
def f1():
    pass
f1()
print('*****')
f1()
print('*****')

print('P2-装饰函数不带参数，被装饰函数带参数')
def decorator_two(f2):
    #定义包装函数，用于传递被装饰函数当做参数，使用可变参数和关键字参数可以提升灵活性
    @functools.wraps(f2)
    def wrapper_two(*args, **kw):
        print('start')
        print('call ' + f2.__name__)
        f2(*args, **kw)
        print('end')
       # return f2 *******在函数中使用了被装饰函数，就不用再返回这个函数了，因为已经被执行过了*******
    return wrapper_two

@decorator_two
def f2(s):
    print(s)

f2('test')
print('*****')
f2('test')
print('*****')

print('P3-装饰函数带参数，被装饰函数不带参数')
#装饰函数外层加一层函数，用来传递装饰函数的参数
def my_decorator_three(*args,**kw):
    #这里才是装饰函数开始的地方，传入装饰函数参数f3
    def decorator_three(f3):
        # @functools.wrap(f3) 这句在这里可加可不加，反正不会出现函数名字指定错误
        print('start')
        print('f3的装饰器函数自带参数为:',*args)
        print('call ' + f3.__name__)
        print('end')
        return f3
    return decorator_three

@my_decorator_three('my_decorator_three')
def f3():
    pass

f3()
print('*****')
f3()
print('*****')

print('P4-装饰器函数和被装饰函数都带参数')
#这层传递的参数是装饰函数本身需要使用的参数
def my_decorator_four(*args_decorator,**kw_decorator):
    #这一层函数传递需要被装饰的函数f4
    def decorator_four(f4):
        @functools.wraps(f4)
        #这一层包装函数用于传递被装饰函数f4所需要的参数
        def wrapper(*args,**kw):
            print('start')
            print('f4的装饰器函数自带参数为:',*args_decorator)
            print(f4.__name__ + ' is working')
            #在这个函数内已经使用了带参数的被装饰函数f4,所以最后也不需要返回函数f4了
            f4(*args, **kw)
            print('end')
        return wrapper
    return decorator_four

@my_decorator_four('my_decorator_four')
def f4(s):
    print(s)

f4('test')
print('*****')
f4('test')
print('*****')

print('P5-习题，设计一个装饰函数带可变参数，被装饰函数不带参数的装饰器')
def my_decorator_five(*args, **kw):
    def decorator_five(f5):
        print(*args)
        print('begin call')
        #在函数中使用了被装饰函数，就不用再返回这个函数了，因为已经在这被执行过了
        print(f5.__name__ + ' is working')
        print('end call')
        return f5
    return decorator_five

@my_decorator_five()
def f5():
   print('test') 

f5
print('*****')
f5()
print('*****')

print('=================')
@my_decorator_five('execute')
def f6():
    print('test') 

f6
print('*****')
f6()
print('*****')
print('=================')
print(f1.__name__)
print(f2.__name__)
print(f3.__name__)
print(f4.__name__)
print(f5.__name__)
print(f6.__name__)
