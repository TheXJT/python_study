# -*- coding: utf-8 -*-
#利用filter过滤寻找回文数
def is_palindrome(n):
    return str(n)[::-1]==str(n)
output=filter(is_palindrome, range(1000,10000))
print(list(output))
