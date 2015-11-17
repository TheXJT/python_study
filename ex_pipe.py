#encoding=utf-8
from multiprocessing import Process,Pipe
import os,time,random

def write(conn):
    print('Process to write: %s' % os.getpid())
    for value in['A','B','C']:
        print('Put %s to queue...' %value)
        conn.send('This is a message!')
        time.sleep(random.random())

def read(conn):
    print('Process to write: %s' % os.getpid())
    while True:
        value=conn.recv()
        print('Get %s from queue.' % value)

if __name__=='__main__':
    conn1,conn2=Pipe()
    pw=Process(target=write,args=(conn1,))
    pr=Process(target=read,args=(conn2,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
