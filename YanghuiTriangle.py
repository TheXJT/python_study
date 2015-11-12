# -*- coding: utf-8 -*-
#利用generator生成杨辉三角
def triangles_1():
    b=[1]
    while True:
        yield b
        b=[1]+[b[i]+b[i+1] for i in range(len(b)-1)]+[1]

def triangles_2():
    b=[1]
    while True:
        yield(b)
        b2=b[:]
        for i in range(1,len(b)):
                b[i]=b2[i-1]+b2[i]
        b.append(1)

n=0
for t in triangles_2():
    print(t)
    n+=1
    if n==10:
        break
