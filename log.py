# -*- coding: utf-8 -*-
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call %s():' % func.__name__)
        func(*args, **kw)
        print('end call %s():' % func.__name__)
        return
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def now():
    print('xjt')
print('==== 1 ====')
now()
print('==== 2 ====')
now()

@log2('execute')
def now2():
    print('xjt')
print('==== 1 ====')
now2()
print('==== 2 ====')
now2()
