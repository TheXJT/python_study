# from random import randint

# def d6():
# 	return randint(1,6)

# d6_iter=iter(d6,1)

all=open('D:\\青海克贡玛\\矿权\\1.txt','w',encoding='utf-8')
all.write('id | 矿权名称 | 许可证号 | 坐标系 | Y | X\n')

with open('D:\\青海克贡玛\\矿权\\矿权查询.txt') as fp:
	flag=fp.readline()
	while "end" not in flag:
		s=[]
		for line in iter(fp.readline,'    0,0\n'):
			s.append(line[:-1])
		temp=s[0].split()
		id=temp[0]
		if '许可证号为' in temp[1]:
			name=temp[1][:temp[1].find('(')]
			license=temp[1][temp[1].find('为:')+3:temp[1].find(')')]
		else:
			name=temp[1]
			license=""
		corrd=s[1][s[1].find('(')+1:s[1].find(')')]
		fmt='{:10}|{:20s}|{:20s}|{:10s}|{:20}|{:20}\n'
		fmt2='{:10}|{:20s}|{:20s}|{:10s}\n'
		for i in range(2,len(s)):
			t=s[i]
			y=t[:t.find(',')]
			x=t[t.find(',')+1:]
			out=fmt.format(id,name,license,corrd,y,x)
			all.write(out)
		all.write(fmt2.format(id,name,license,corrd))
		flag=fp.readline()
all.close()