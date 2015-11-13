#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module ' #表示模块的文档注释

__author__='TheXJT' #作者

import sys

def test(*arg):
    args=sys.argv #sys.argv变量用list存储了命令行的所有参数,args[0]=filename
    print(*arg)
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

#当在运行模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该模块时，if判断将失效，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
if __name__=='__main__':
    test()
    print(__name__)
    print(__author__)
    print(__doc__)
