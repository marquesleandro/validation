# =======================
# Importing the libraries
# =======================


import numpy as np
from tqdm import tqdm
from time import time
import matplotlib.pyplot as plt

print '------------'
print 'COMPARATION:'
print '------------'

start_time = time()

# -----
# 0.1 s
# -----

cav_num = []
with open('couette1.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

nn = 50
y1 = np.zeros([nn,1], dtype = float)
vx1 = np.zeros([nn,1], dtype = float)
for i in range(1,nn-1):
 aa = int(len(cav_num)/nn)
 vx1[i] = cav_num[i*aa][1]
 y1[i] = cav_num[i*aa][7]

vx1[0] = -1.0
vx1[nn-1] = 1.0
y1[0] = 0.0
y1[nn-1] = 1.0

# -----
# 0.2 s
# -----

cav_num = []
with open('couette0.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

nn = 50
y2 = np.zeros([nn,1], dtype = float)
vx2 = np.zeros([nn,1], dtype = float)
for i in range(1,nn-1):
 aa = int(len(cav_num)/nn)
 vx2[i] = cav_num[i*aa][1]
 y2[i] = cav_num[i*aa][7]

vx2[0] = -1.0
vx2[nn-1] = 1.0
y2[0] = 0.0
y2[nn-1] = 1.0





# -----
# 1 s
# -----

cav_num = []
with open('couette5.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y3 = np.zeros([len(cav_num)-1,1], dtype = float)
vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx3[i-1] = cav_num[i][1]
 y3[i-1] = cav_num[i][7]

# ------------
# Steady State
# ------------

cav_num = []
with open('couette.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y4 = np.zeros([len(cav_num)-1,1], dtype = float)
vx4 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx4[i-1] = cav_num[i][1]
 y4[i-1] = cav_num[i][7]


# -----
# exact
# -----
vxe = np.zeros([200,1], dtype = float)
ye = np.zeros([200,1], dtype = float)

U_top = 1.0
U_bottom = - 1.0
L = 1.0
for i in range(0,200):
 ye[i] = (i/200.0)
 vxe[i] = (U_top - U_bottom)*(ye[i]/L) + U_bottom



end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""


plt.clf()
plt.rc('text', usetex=True)
plt.rc('font', family='fourier')
ax = plt.axes()
ax.set_xlabel(r'Horizontal Velocity',fontsize=14)
ax.set_ylabel(r'y',fontsize=14)
ax.set_aspect('auto')
plt.plot(vx2, y2, '2', color='black', fillstyle='none', label = "t = 0.1")
plt.plot(vx1, y1, '.', color='black', label = "t = 0.5")
plt.plot(vx4, y4, '--', color='black', label = "numerical solution")
plt.plot(vxe, ye, '-', color='black', label = "analytical solution")
plt.legend(loc = 4)
plt.show()

