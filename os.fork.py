import os
print('Process (%s) start...' % os.getpid())
pid=os.fork() #fork()函数生成了一个子进程，返回值pid有两个，一个为0，用以表示子进程，一个是大于0的整数，用以表示父进程
if pid==0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s).' %(os.getpid(),pid))
