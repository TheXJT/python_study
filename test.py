# print(divmod(20,8))
t=(20,8)
print(divmod(*t))
quotient,remainder=divmod(*t)
print(quotient,remainder)

import os
path,filename=os.path.split('~/python_study/test.py')
print(filename)
print(path)

a,b,*rest=range(3)
print(type(a),type(b),type(rest))