#-*- coding: utf-8 -*-
import os
import sys
def test():
    args=sys.argv
    if len(args)==2:
        return args[1]
    else:
        print('arguments error!')

#查找目录下是否有指定文件
def find_dir(dirs,filename):
    file=[x for x in os.listdir(dirs) if os.path.isfile(os.path.join(dirs,x))]
    path=[]
    for file1 in file:
        if filename in file1: #查找文件名中包含filename的文件
             path.append(os.path.join(os.path.abspath(dirs),file1))
        else:
            pass
    return path

#查找当前目录及子目录下的文件
def find_file(filename):
    dir=[x for x in os.listdir('.') if os.path.isdir(x)]
    dir.append(os.getcwd()) #将当前文件夹包括进来
    for subdir in dir:
        dir_name=find_dir(subdir,filename)
        if(dir_name):
            for i in dir_name:
                print(i)
        else: 
            pass

if __name__=='__main__':
    filename=test()
    find_file(filename)
