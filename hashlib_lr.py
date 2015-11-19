#-*- coding: utf-8 -*-
import hashlib
db={}

def get_md5(str):
    md5=hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

def register(user, pw):
    db[user]=get_md5(pw+user+'the_Salt')
    print('User %s has been registered successfully' % user)

def login(user, pw):
    if(user in db):
        if get_md5(pw+user+'the_Salt')==db[user]:
            print('User %s login successfully' % user)
        else:
            print('Password incorrect!')
    else:
        print('User %s doesn\'t exist' % user)

if __name__=='__main__':
    while True:
        n=input('Choose your action, 1 or 2:\n1. Login\n2. Register\n')
        if n=='1':
            username=input('Please enter your username: ')
            pw=input('Please enter your password: ')
            login(username,pw)
        elif n=='2':
            username=input('Please enter your username: ')
            pw=input('Please enter your password: ')
            register(username,pw)
        else:
            exit(0)
