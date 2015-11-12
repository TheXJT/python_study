# -*- coding: utf-8 -*-
#print('函数操作实现')
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n+=1
    return 'done'
#print('generator 实现')
def fib_ge(max):
    n,a,b=0,0,1
    while n<max:
        yield b  #如果一个函数定义中包含yield关键字，那么这个函数不再是一个普通函数，而是一个generator
        a,b=b,a+b
        n+=1
    return 'done'

def odd():
    print('step 1')
    yield(1) 
    print('step 2')
    yield(3) 
    print('step 3')
    yield(5)
