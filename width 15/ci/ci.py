import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
import random

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			    			# width  in inches
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
threshold = 0.20
width = 15.0
size = 28 
threshold2 = threshold*threshold
mass = 70.0
diameter = 0.47
sigma_diameter = 0.03



def aleja(xi,yi,x,y):
     flag = 1
     i=0
     while i<len(x) and flag:
          dist2 = (x[i]-xi)*(x[i]-xi) +(y[i]-yi)*(y[i]-yi)
          if dist2<threshold2:
               flag = 0 
          i+=1
     return flag

def agrega_pedestrian(x,y):
     xi = random.uniform(0.5, size-0.2)
     yi = random.uniform(0.5, width-0.2)
     if not aleja(xi,yi,x,y):
     	agrega_pedestrian(x,y)
     else:
     	x+=[xi]
     	y+=[yi]
     return [x,y]


####### MAIN ##################

for density in range(1,10):
	N = density*size*width
	N = int(N)
	vector_diameter = np.random.normal(diameter, sigma_diameter, N)
	x = [random.uniform(0.5, size-0.5)]
	y = [random.uniform(0.5, width-0.5)]

	for i in range(1,N):
		resultado = agrega_pedestrian(x,y)
		x = resultado[0]
		y = resultado[1]


	###  OUTPUT  ###
	f= open("ci_pasillo_15m_density_%d.txt"%density,"w+")

	f.write("# LAMMPS data file for rigid bodies\n\n")
	f.write("%d atoms\n\n"%N)
	f.write("2 atom types\n\n")
	f.write("%2.1f \t %2.1f \t xlo xhi \n"%(0.0, size)) 			
	f.write("%2.1f \t %2.1f \t ylo yhi \n"%(0.0, width))
	f.write("%2.1f \t %2.1f \t zlo zhi \n\n"%(-1, 1))
	f.write("Atoms\n\n")

	for i in range(0,N):
	     f.write("%d %d %2.2f %2.2f %2.4f %2.4f %d \n" % ((i+1), 1 ,vector_diameter[i],mass ,x[i],y[i],0))


	###  PLOT  ###

	pylab.grid(False)


	plt.plot(x,y,'og',zorder=3,markersize='0.46')  
	#pylab.grid(True)

	pylab.xlabel('x ')
	pylab.ylabel('y')
	pylab.savefig('ci_pasillo_15m_density_%d.eps'%density, format='eps', dpi=300, bbox_inches='tight')