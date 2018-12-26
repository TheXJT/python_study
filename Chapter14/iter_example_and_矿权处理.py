from random import randint

def d6():
	return randint(1,6)

d6_iter=iter(d6,1)
# print(d6_iter)
# for roll in d6_iter:
	# print(roll)
 
with open('D:\青海克贡玛\矿权\矿权查询.txt',encoding="GB2312") as fp:
	while True:
		s=[]
		for line in iter(fp.readline,'    0,0\n'):
	 		s.append(line[:-1].split())
		print(s[1][0])