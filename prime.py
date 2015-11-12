# -*- coding: utf-8 -*-
def _odd_iter(): #构造一个从3开始的奇数序列
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n): #定义的筛选函数
    return lambda x: x % n > 0 # % 求模运算

def primes():
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n=next(it) #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) #构造新序列

for n in primes():
    if n< 20:
        print(n)
    else:
        break
