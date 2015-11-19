#-*- coding: utf-8 -*-
import base64, os, sys
def test():
    args=sys.argv
    if len(args)==2:
        return args[1]
    else:
        print('arguments error!')

def safe_base64_decode(s):
    try:
        s1=s+b'='*(4-len(s)%4)
    except:
        s1=s+'='*(4-len(s)%4)
    return(base64.urlsafe_b64decode(s1))

if __name__=='__main__':
    code=test()
    print(code)
    print(safe_base64_decode(code))
