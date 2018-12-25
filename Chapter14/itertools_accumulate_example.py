sample=[5,4,2,8,7,6,3,0,9,1]
import itertools
a=list(itertools.accumulate(sample))
print(a)
a=list(itertools.accumulate(sample,min))
a=list(itertools.accumulate(sample,max))
import operator
a=list(itertools.accumulate(sample,operator.mul))
a=list(itertools.accumulate(range(1,11),operator.mul))
a=list(enumerate('albatroz',3))
a=list(map(operator.mul,range(11),[2,4,8]))
a=list(map(lambda a,b:(a,b),range(11),[2,4,8]))
a=list(itertools.starmap(operator.mul,enumerate('albatroz',1)))
a=list(itertools.starmap(lambda a,b:b/a,enumerate(itertools.accumulate(sample),1)))

print(a)