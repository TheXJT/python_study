#-*- coding: utf-8 -*-
from functools import reduce
def normalize(name):
    L=name[0].upper()
    for x in name[1:]:
        L+=x.lower()
#    return(name[:1].upper()+name[1:].lower())
    return(L)
def str2float(s):
    return reduce(lambda x, y: x+y*(0.1**len(str(y))),map(int,s.split('.')))
print('格式化不标准输入的名字')
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)
print('str2float:\'123.456\'')
print(str2float('123.456'))
