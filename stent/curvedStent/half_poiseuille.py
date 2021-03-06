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
'''
# -----
# 0.1 s
# -----

cav_num = []
with open('half_poiseuille_20b.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y1 = np.zeros([len(cav_num)-1,1], dtype = float)
vx1 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx1[i-1] = cav_num[i][1]
 y1[i-1] = cav_num[i][7]
'''
# -----
# 0.2 s
# -----

cav_num = []
with open('quadGeovel05.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

#y2 = np.zeros([len(cav_num)-1,1], dtype = float)
#vx2 = np.zeros([len(cav_num)-1,1], dtype = float)
#for i in range(1,len(cav_num)):
# vx2[i-1] = cav_num[i][1]
# y2[i-1] = cav_num[i][7]


nn = 50
y2 = np.zeros([nn,1], dtype = float)
vx2 = np.zeros([nn,1], dtype = float)
for i in range(1,nn-1):
 aa = int(len(cav_num)/nn)
 vx2[i] = cav_num[i*aa][1]
 y2[i] = cav_num[i*aa][7]

vx2[0] = 0.0
vx2[nn-1] = 1.87
y2[0] = 0.6
y2[nn-1] = 0.0





# -----
# 1 s
# -----

cav_num = []
with open('quadGeovel1.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

#y3 = np.zeros([len(cav_num)-1,1], dtype = float)
#vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
#for i in range(1,len(cav_num)):
# vx3[i-1] = cav_num[i][1]
# y3[i-1] = cav_num[i][7]

nn = 50
y3 = np.zeros([nn,1], dtype = float)
vx3 = np.zeros([nn,1], dtype = float)
for i in range(1,nn-1):
 aa = int(len(cav_num)/nn)
 vx3[i] = cav_num[i*aa][1]
 y3[i] = cav_num[i*aa][7]

vx3[0] = 2.079
vx3[nn-1] = 0.0
y3[0] = 0.0
y3[nn-1] = 0.6




# ------------
# Steady State
# ------------

cav_num = []
with open('quadGeovel100.csv') as cav:
#with open('half_poiseuille1.csv') as cav:
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

u_max = 1.5
L = 1.0
for i in range(0,200):
 ye[i] = (i/200.0)
 vxe[i] = u_max*(1.0 - (ye[i]/L)**2)

print len(y4)
print len(ye)
print len(y4)/len(ye)
factor = len(y4)/len(ye)

'''
erro = []
for i in range(0,len(y4)-1):
 err = np.sqrt((vxe[i/factor] - vx4[i])**2)
 erro.append(err)

avg_erro = sum(erro)/len(erro)

print avg_erro
'''

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
#plt.plot(vx1, y1, '2', color='black', label = "t = 0.1")
plt.plot(vx2, y2, '.', color='black', label = "t = 0.5s")
plt.plot(vx3, y3, '--', color='black', label = "t = 1.0s")
plt.plot(vx4, y4, '-', color='black', label = "t = 100.0s")
#plt.plot(vxe, ye, '-', color='black', label = "analytical solution")
plt.legend(loc = 3)
#tikzplotlib.save("horizontalVelocity.tex")
plt.show()

