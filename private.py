# -*- coding: utf-8 -*-
def __private_1(name):
    return'Hello, %s' %name
def __private_2(name):
    return 'Hi, %s' %name

def greeting(name):
    if len(name)>3:
        print(__private_1(name))
    else:
        print(__private_2(name))

if __name__=='__main__':
    greeting('xujiatian')
    greeting('Bob')
    greeting('Ad')
