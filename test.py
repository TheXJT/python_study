import random
import math
class p:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def line(step=0,direct=0):
		s = '@%s<%s'%(step,direct)
		return s
	def line2(p1,p2):
		s = '%s,%s %s,%s '%(p1.x,p1.y,p2.x,p2.y)
		return s
	def box(p,a,b,c):
		s = 'box %s,%s l %s %s %s '%(p[0],p[1],a,b,c)
		return s
	def saibotancell(step = 4,direct = 60):
		step1 = random.randint(5,8)
		direct1 = random.randint(0,5) *60
		s =''
		s += line(step=step1,direct=direct1)
		return s
	def sai(seed = 10000):
		sai_text = 'L 0,0\n'
		n = 0
		while n < seed:
			sai_text += str(saibotancell())+'\n'
			n += 1
			return sai_text
	def saistarcell():
		p1_rand = random.randint(5,8)
		p2_rand = random.randint(8,20)
		p_sita = math.pi*2*random.random()
		x1 = p1_rand*math.cos(p_sita)
		y1 = p1_rand*math.sin(p_sita)
		x2 = p2_rand*math.cos(p_sita)
		y2 = p2_rand*math.sin(p_sita)
		p1 = p(x1,y1)
		p2 = p(x2,y2)
		s =''
		s += line2(p1,p2)
		return s
	def saistar(seed = 1000):
		n = 0
		saistar_text = 'L '
		for i in range(seed):
			saistar_text += str(saistarcell())+'\n'
		return saistar_text
	def chaoscitycell():
		x = position_rand = random.randint(0,1000)
		y = position_rand = random.randint(0,1000)
		p1 = p(x,y)
		a = random.randint(0,30)+30
		b = a*random.randint(10,22)/10
		c = random.randint(15,300)
		s = ''
		s += str(box([p1.x,p1.y],a,b,c))
		return s
	def chaoscity(seed = 100):
		n = 0
		chaoscity_text = 'box '
		for i in range(seed):
			chaoscity_text += chaoscitycell()+'\n'
			return chaoscity_text
	def circle_line(seed = 100):
		step = 0
		direct = 0
		s = 'l 0,0 '
		for i in range(seed):
			if i %2 ==0:
				step += 1
			if direct >=270:
				direct = 0
		s += line(step=step,direct=direct)+' '
		direct += 90
		return s
f = open(r'cad.txt',mode = 'w')
#赛博坦星球表面
#f.write(sai())
#赛博坦之心
#f.write(saistar())
#混乱都市
#f.write(chaoscity())
#回宫格
#f.write(circle_line())
f.close()