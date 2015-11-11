# -*- coding: utf-8 -*-
#汉诺塔问题解决程序：利用递归函数
def move(n,a,b,c):
    to='-->'
    if n==1:
        print(a,to,c)
    else:
        move(n-1,a,c,b)
        print(a,to,c)
        move(n-1,b,a,c)

move(3,'A','B','C')
