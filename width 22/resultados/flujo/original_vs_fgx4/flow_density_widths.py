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
data_modified = np.genfromtxt("flow-density_vd1_pasillo22m_fgx4.txt",delimiter = ' ') 
density_modified = data_modified[:,0]
flow_modified = data_modified[:,1]

data_original = np.genfromtxt("flow-density_vd1_pasillo22m_original.txt",delimiter = ' ') 
density_original = data_original[:,0]
flow_original = data_original[:,1]



###  PLOT  ###

pylab.figure(1)
pylab.clf()

plt.plot(density_original,flow_original,'-ob',markersize=3.5,label='Original')
plt.plot(density_modified,flow_modified,'-og',markersize=3.5,label='Fg  x4')

pylab.grid(False)
#pylab.xlabel('time~$(s)$')
pylab.xlabel('Density~(p~/m$^{2}$)')
pylab.ylabel('Flow~(p~/m/s)')
#pylab.legend()
#pylab.ylim(0.0, 60.0)
#pylab.ylim(0.0, 3.6)
#pylab.yticks(np.arange(3,11,2))
#pylab.xlim(0.5, 8)
#pylab.xticks(np.arange(0,1100,200))
pylab.xlim(0, 10.1)
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(loc='upper left',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 
pylab.savefig('flow-density_original_vsfgwall_modified.png', format='png', dpi=300, bbox_inches='tight')