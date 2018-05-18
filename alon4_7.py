import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math

# Model for Coherent FFL

# Step Function
theta_xy = 1
theta_xz = 1
theta_yz = 1

# Rate of Production
alpha_y = 1
alpha_z = 1
beta_y = 1
beta_z = 1

# R_y = beta_y * theta_xy - alpha_y * Y
# R_z = beta_z * theta_xz * theta_yz - alpha_z * Z

t = np.linspace(-0.5,2.5,7)
S_x = [0, 1, 1, 1, 1, 1, 1]
t_y = np.linspace(-0.5,2.5,100)
# print t_y
Y_st = beta_y/alpha_y
Z_st = beta_z/alpha_z
Y =[]
for i in range(len(t_y)):
	if(t_y[i]<0):
		Y.append(0)
	else:
		Y.append(Y_st * (1 - math.exp(-alpha_y * t_y[i])))


Zo =[]
for i in range(len(t_y)):
	if(t_y[i]<0.6):
		Zo.append(0)
	else:
		Zo.append(Z_st * (1 - math.exp(-alpha_z * (t_y[i] - 0.6))))

# Z =[]
# for i in range(len(t_y)):
# 	if(t_y[i]<0.6):
# 		Z.append(0)
# 	else:
# 		Z.append(Z_st + (Zo[i] - Z_st) * (math.exp(-alpha_z * (t_y[i]-1.19))))


fig = plt.figure(figsize=(10, 9))
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 1])

ax0 = fig.add_subplot(gs[1, 0])
ax0.plot(t_y, Y,'-')
ax0.set_title('Activation of Y')
ax0.set_ylabel('Active Y')

# ax0.xlabel('time')
# ax0.ylabel('Activated Y')
# ax1.axis([-0.5,2.5,-0.5,1.5])
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(t, S_x, drawstyle='steps-post', linestyle='-', alpha=0.5)
ax1.set_title('Input Stimuli for X')
ax1.set_ylabel('S_x')



ax2 = fig.add_subplot(gs[2, 0])
ax2.plot(t_y, Zo,'-')
ax2.set_title('Activation of Z')
ax2.set_xlabel('time')
ax2.set_ylabel('Active Z')


# ax1.xlabel('time')
# ax1.ylabel('S_x')
# ax1.axis([-0.5,2.5,-0.5,1.5])


plt.tight_layout()
plt.show()