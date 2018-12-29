import matplotlib.pyplot as plt
import numpy as np
x_train = np.array([100,80,120,75,60,43,140,132,63,55,74,44,88])
y_train = np.array([120,92,143,87,60,50,167,147,80,60,90,57,99])
# x_train = np.array(range(10))
# y_train = np.array(range(10))

alpha=0.0000001
cnt=0
m=len(x_train)
theta0=0
theta1=0
error0=0
epsilon=0.0000001

def h(x):
	return theta1*x+theta0

while True:
	cnt=cnt+1
	diff=[0,0]
	t=h(x_train)-y_train
	diff[0]=sum(t)
	diff[1]=sum(t*x_train)
	theta0-=alpha*diff[0]/m
	theta1-=alpha*diff[1]/m

	error1=np.linalg.norm(y_train-h(x_train))
	if abs(error1 - error0) < epsilon:
		break
	else:
		error0=error1

plt.plot(x_train,[h(x) for x in x_train])
plt.plot(x_train,y_train,'bo')
print(theta1,theta0,error0)
plt.show()