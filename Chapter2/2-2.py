symbols='$!@#$^^^'
temp=tuple(ord(symbol) for symbol in symbols)

import array
temp=array.array('I',(ord(symbol) for symbol in symbols))

print(temp)
print(temp[0])