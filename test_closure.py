#-*- coding: utf-8 -*-
def test():
    a=0
    def return_func():
        nonlocal a
        a=a+1
        return a
    return return_func
t=test()
print(t())
