import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math


t = np.linspace(0,20,40)
# print len(t)

S_x = [0]
for i in range(len(t)):
	if(t[i]<2.5):
		S_x.append(0)
	elif(3<t[i]<4):
		S_x.append(1)
	elif(4<t[i]<10):
		S_x.append(0)
	elif(10<t[i]<14.5):
		S_x.append(1)
	elif(t[i]>14.5):
		S_x.append(0)
# print len(S_x)

# Step Function
theta_xy = 1
theta_xz = 1
theta_yz = 1

# Rate of Production
alpha_y = 1
alpha_z = 1
beta_y = 1
beta_z = 1


t_y = np.linspace(0,20,1000)

print len(t_y)
# print t_y
Y_st = beta_y/alpha_y
Z_st = beta_z/alpha_z

Y =[]
for i in range(len(t_y)):
	if(t_y[i]<2.6):
		Y.append(0)
	elif(2.6<t_y[i]<4):
		Y.append(Y_st * (1 - math.exp( 2.5 -alpha_y * t_y[i])))
	elif(4<t_y[i]<10):
		Y.append(Y_st * (math.exp(-alpha_y * (t_y[i] - 3.7))))
	elif(10<t_y[i]<14.5):
		Y.append(Y_st * (1 - math.exp( 5-alpha_y * (t_y[i] - 5))))
	elif(t_y[i]>14.5):
		Y.append(Y_st * (math.exp(-alpha_y * (t_y[i] - 14.505))))


Zo =[]
for i in range(len(t_y)):
	if(t_y[i]<10.2):
		Zo.append(0)
	elif(10.2<t_y[i]<14.5):
		Zo.append(Z_st * (1 - math.exp(10.2 -alpha_z * (t_y[i]))))
	elif(t_y[i]>14.5):
		Zo.append(Z_st * (math.exp(-alpha_z * (t_y[i] - 14.5))))



fig = plt.figure(figsize=(10, 9))
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 1])


ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(t, S_x, drawstyle='steps-post', linestyle='-', alpha=0.5)
ax1.set_title('Input Stimuli for X')
ax1.set_ylabel('S_x')

ax0 = fig.add_subplot(gs[1, 0])
ax0.plot(t_y, Y,'-')
ax0.set_title('Activation of Y')
ax0.set_ylabel('Active Y')

ax2 = fig.add_subplot(gs[2, 0])
ax2.plot(t_y, Zo,'-')
ax2.set_title('Activation of Z')
ax2.set_xlabel('time')
ax2.set_ylabel('Active Z')



plt.tight_layout()
plt.show()