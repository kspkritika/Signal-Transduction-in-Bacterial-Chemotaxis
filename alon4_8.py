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


t = np.linspace(-1,2.5,8)
S_x = [1, 1, 0, 0, 0, 0, 0, 0]
t_y = np.linspace(-1,2.5,100)
print t

Y_st = beta_y/alpha_y
Z_st = beta_z/alpha_z
Y =[]
for i in range(len(t_y)):
	if(t_y[i]<0):
		Y.append(1)
	else:
		Y.append(Y_st * (math.exp(-alpha_y * (t_y[i]))))

Zo =[]
for i in range(len(t_y)):
	if(t_y[i]<0):
		Zo.append(1)
	else:
		Zo.append(Z_st * (math.exp(-alpha_z * (t_y[i]))))

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

# # Ratio of K_yz and Y_st
# x = np.linspace(0,1,100)

# # Delay in Z Production
# y = []
# for i in range(len(x)):
# 	y.append(math.log(1/(1-x[i])))

# plt.plot(x, y, 'm')
# plt.title('Delay in Z Production')
# plt.xlabel('K_yz/Y_st')
# plt.ylabel('Delay in Z Production')
# plt.axis([0,1,0,5])
# fig = plt.gcf()
# plt.legend()
# plt.show()