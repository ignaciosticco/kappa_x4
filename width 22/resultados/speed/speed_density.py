# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

'''

'''

import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
#import numarray

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			    # width  in inches
fig_height = fig_width*golden_mean          # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
          'axes.linewidth': 0.5, 
          'axes.grid': True,
          'axes.labelweight': 'normal',  
          'font.family': 'serif',
          'font.size': 8.0,
          'font.weight': 'normal',
          'text.color': 'black',
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'legend.fontsize': 8,
          'figure.dpi': 300,
          'figure.figsize': fig_size,
          'savefig.dpi': 300,
         }

pylab.rcParams.update(params)

### DATA ###
speed = []
density = []
for i in range(1,10):
	data = np.genfromtxt("density_%d_speedhelbing_vd1_pasillo.txt"%i,delimiter = ' ') 
	density_raw = data[:,2]
	speed_raw = data[:,3]
	fin = len(density_raw)-1
	inicio = fin-5
	density+=[np.mean(data[inicio:fin,2])]
	speed+=[np.mean(data[inicio:fin,3])]

print(speed)

### OUTPUT ###
N = len(speed)
output = np.zeros([N,2])
for i in range(0,N):
     output[i,0] = density[i]
     output[i,1] = speed[i]

np.savetxt('speed-density_vd1_pasillo15m.txt', output,fmt='%.2f', delimiter=' ') 
###  PLOT  ###

pylab.figure(1)
pylab.clf()

plt.plot(density,speed,'ob',markersize=3.5)

pylab.grid(False)
#pylab.xlabel('time~$(s)$')
pylab.xlabel('Density~(p~/m$^{2}$)')
pylab.ylabel('speed~(m/s)')
#pylab.legend()
#pylab.ylim(0.0, 60.0)
#pylab.ylim(0.00, 2.0)
#pylab.yticks(np.arange(3,11,2))
#pylab.xlim(0, 10)
#pylab.xticks(np.arange(0,1100,200))
#pylab.xlim(0, 8)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
#plt.legend(loc='upper right',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1)
pylab.savefig('speed_density_pasillo_vd1.eps', format='eps', dpi=300, bbox_inches='tight')
