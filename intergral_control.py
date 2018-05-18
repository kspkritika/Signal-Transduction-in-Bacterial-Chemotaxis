import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import scipy.io as spio


mat = spio.loadmat('RRmatlab.mat', squeeze_me=True)

R = mat['ans'] # array
# print len(R)


cAMP = 1000
R1_tot = 0.1;
R2_tot = 0.9;
kR1 = 0.00267;
k_R1 = 0.16;
kR2 = 0.00244;
k_R2 = 1.1;
r1 = 0.012;
r2 = 0.115;
kGEF = 0.04;
k_GEF = 0.4;
kGAP = 0.01;
k_GAP = 0.1;
Ras_tot = 1;
kRas = 390;
k_Ras = 3126;
RBD_tot = 1;
koff = 0.53;
kon = 1;
Tend = 30;
# R = [ 0.0959, 1.2700, 1.1550, 4.4050, 0.7000, 0.2050, 1.1600]

t = np.linspace(0,30,len(R))

GEF1a = []
GAP1a = []
Ras1a = [0]
Ras1b = [0]
GAP2a = [0]
GAP2b = [0]
GEF2a = []
GEF2b = []
Ras2a = []
Ras2b = []
GEF3a = []
GEF3b = []
GAP3a = [0]
GAP3b = [0]
Ras3a = []
Ras3b = []
GEF4a = []
GAP4a = [0]
GEF4b = []
GAP4b = [0]
Ras4a = []
Ras4b = []
GAP5a = [0]
GAP5b = [0]
GEF5a = []
GEF5b = []
Ras5a =[]
Ras5b = []
GEF6a = []
GAP6a = [0]
GEF6b = []
GAP6b = [0]
Ras6a = []
Ras6b = []

# Calculations at steady state. Assuption GAP1a gets a fixed initial value
for i in range(len(R)):
	GEF1a.append(kGEF * R[i] / k_GEF)
	GAP1a.append(Ras1a[i])
	Ras1a.append(min(GEF1a[i], 1 - GAP1a[i]))
	Ras1b.append(max(GEF1a[i], 1 - GAP1a[i]))

	GEF2a.append(min(kGEF * R[i] / k_GEF , 1 - GAP2a[i]))
	GAP2a.append(GEF2a[i])
	Ras2a.append(GEF2a[i])
	GEF2b.append(max(kGEF * R[i] / k_GEF , 1 - GAP2b[i]))
	GAP2b.append(GEF2b[i])
	Ras2b.append(GEF2b[i])

	GEF3a.append(min(kGEF * R[i] / k_GEF , 1 - GAP3a[i]))
	Ras3a.append(GEF3a[i])
	GAP3a.append(Ras3a[i])

	GEF3b.append(max(kGEF * R[i] / k_GEF , 1 - GAP3b[i]))
	Ras3b.append(GEF3b[i])
	GAP3b.append(Ras3b[i])

	GEF4a.append(kGEF * R[i] / k_GEF)
	Ras4a.append(min(GEF4a[i], GAP4a[i]))
	GAP4a.append(1 - Ras4a[i])

	GEF4b.append(kGEF * R[i] / k_GEF)
	Ras4b.append(max(GEF4b[i], GAP4b[i]))
	GAP4b.append(1 - Ras4b[i])

	GEF5a.append(min(kGEF * R[i] / k_GEF, GAP5a[i] ))
	Ras5a.append(GEF5a[i])
	GAP5a.append(1 - Ras5a[i])

	GEF5b.append(max(kGEF * R[i] / k_GEF, GAP5b[i] ))
	Ras5b.append(GEF5b[i])
	GAP5b.append(1 - Ras5b[i])

	GEF6a.append(min(kGEF * R[i] / k_GEF, GAP6a[i]))
	GAP6a.append(1 - GEF6a[i])
	Ras6a.append(GEF6a[i])

	GEF6b.append(min(kGEF * R[i] / k_GEF, GAP6b[i]))
	GAP6b.append(1 - GEF6b[i])
	Ras6b.append(GEF6b[i])

# print Ras1a
# print Ras1b
# print Ras2a 
# print Ras2b 
# print Ras3a 
# print Ras3b 
# print Ras4a 
# print Ras4b 
# print Ras5a  
# print Ras5b
# print Ras6a  
# print Ras6b



del Ras1a[-1]
del Ras1b[-1]
del GAP2a[-1]
del GAP2b[-1]
del GAP3b[-1]
del GAP3a[-1]
del GAP4a[-1]
del GAP4b[-1]
del GAP5a[-1]
del GAP5b[-1]
del GAP6a[-1]
del GAP6b[-1]

# print len(Ras6b)
# print len(GEF6b)
# print len(GAP6b)

fig = plt.figure(figsize=(15, 9))
gs = gridspec.GridSpec(nrows=2, ncols=2, height_ratios=[1]*2)

ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(t, Ras5a, 'm', label = 'Ras output for [15,1,2]')
# ax1.plot(t, GEF1a, 'r-', label = 'GEF output for [0,2,9]')
# ax1.plot(t, GAP1a, 'b', label = 'GAP output for [0,2,9]')
ax1.set_ylabel('ON Probability')
ax1.set_xlabel('time')
plt.legend()

ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(t, Ras5b, 'm', label = 'Ras output for [16,1,2]')
# ax2.plot(t, GEF1a, 'r-', label = 'GEF output for [0,2,10]')
# ax2.plot(t, GAP1a, 'b', label = 'GAP output for [0,2,10]')
ax2.set_ylabel('ON Probability')
ax2.set_xlabel('time')
plt.legend()

ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(t, Ras6a, 'm', label = 'Ras output for [15,3,2]')
# ax3.plot(t, GEF2a, 'r-', label = 'GEF output for [13,4,2]')
# ax3.plot(t, GAP2a, 'b', label = 'GAP output for [13,4,2]')
ax3.set_ylabel('ON Probability')
ax3.set_xlabel('time')
plt.legend()

ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(t, Ras6b, 'm', label = 'Ras output for [16,3,2]')
# ax4.plot(t, GEF2b, 'r-', label = 'GEF output for [14,4,2]')
# ax4.plot(t, GAP2b, 'b', label = 'GAP output for [14,4,2]')
ax4.set_ylabel('ON Probability')
ax4.set_xlabel('time')

plt.legend()
plt.tight_layout()
plt.show()

# plt.plot(t, Ras6b, 'm', label = 'Ras')
# plt.plot(t, GEF6b, 'r', label = 'GEF')
# plt.plot(t, GAP6b, 'b', label = 'GAP')
# plt.plot(t, Ras5a,'b', label = 'Network with AND gate')
# plt.title('Integral Control of Ras Pathway using 3 Node Network')
# plt.xlabel('time')
# plt.ylabel('Probability to be ON')
# plt.axis([0,30,0,1])
# fig = plt.gcf()
# plt.legend()
# plt.tight_layout()
# plt.show()
