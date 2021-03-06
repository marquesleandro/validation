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
# Galerkin
# -----

cav_num = []
with open('SLlinear0.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y0 = np.zeros([len(cav_num)-1,1], dtype = float)
vx0 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx0[i-1] = cav_num[i][4]
 y0[i-1] = cav_num[i][6]


cav_num = []
with open('SLlinear1.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y1 = np.zeros([len(cav_num)-1,1], dtype = float)
vx1 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx1[i-1] = cav_num[i][4]
 y1[i-1] = cav_num[i][6]

cav_num = []
with open('SLlinear2.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y2 = np.zeros([len(cav_num)-1,1], dtype = float)
vx2 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx2[i-1] = cav_num[i][4]
 y2[i-1] = cav_num[i][6]

cav_num = []
with open('SLlinear3.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y3 = np.zeros([len(cav_num)-1,1], dtype = float)
vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx3[i-1] = cav_num[i][4]
 y3[i-1] = cav_num[i][6]




# -----
# Exata
# -----

cav_num = []
with open('convection_exact10.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

ye0 = np.zeros([len(cav_num)-1,1], dtype = float)
vxe0 = np.zeros([len(cav_num)-1,1], dtype = float)
ye1 = np.zeros([len(cav_num)-1,1], dtype = float)
vxe1 = np.zeros([len(cav_num)-1,1], dtype = float)
ye2 = np.zeros([len(cav_num)-1,1], dtype = float)
vxe2 = np.zeros([len(cav_num)-1,1], dtype = float)
ye3 = np.zeros([len(cav_num)-1,1], dtype = float)
vxe3 = np.zeros([len(cav_num)-1,1], dtype = float)

for i in range(1,len(cav_num)):
 vxe0[i-1] = cav_num[i][3]
 vxe1[i-1] = cav_num[i][4]
 vxe2[i-1] = cav_num[i][5]
 vxe3[i-1] = cav_num[i][6]
 ye0[i-1] = cav_num[i][7]




end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""

plt.clf()
plt.rc('text', usetex=True)
plt.rc('font', family='fourier')
ax = plt.axes()
ax.set_xlabel(r'position',fontsize=14)
ax.set_ylabel(r'scalar',fontsize=14)
ax.set_aspect('auto')

#ax.xaxis.set_major_locator(plt.MultipleLocator((2* np.pi / 100)))
#ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))


def format_func(value, tick_number):
            # find number of multiples of pi/2
            aa = (2 * value / np.pi)
            N = int(np.round(aa,3))
            print ""
            print aa
            if N == 0:
                return r"$2\pi/5$"
            elif N == 1: #1/4rotation
                return r"$4\pi/5$"
            elif N == 2: #1/2rotation
                return r"$6\pi/5$"
            elif N == 3:
                return r"$8\pi/5$"
            elif N == 4:
                return r"$12\pi/7$"
            elif N == 5: #initial
                return r"$2\pi$"
            elif N == 6:
                return r"$2\pi/7$"
            else:
              return ""





ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))

#plt.plot(y0, vx0, '-', color='black', label = "semi-Lagrangian")
#plt.plot(y1, vx1, '-', color='black', label = "semi-Lagrangian")
#plt.plot(y2, vx2, '-', color='black', label = "semi-Lagrangian")
plt.plot(y3, vx3, '-', color='black', label = "semi-Lagrangian")

#plt.plot(ye0, vxe0, '--', color='black', label = "analytical solution")
#plt.plot(ye0, vxe1, '--', color='black', label = "analytical solution")
#plt.plot(ye0, vxe2, '--', color='black', label = "analytical solution")
plt.plot(ye0, vxe3, '--', color='black', label = "analytical solution")

plt.legend(loc = 1)
plt.show()

