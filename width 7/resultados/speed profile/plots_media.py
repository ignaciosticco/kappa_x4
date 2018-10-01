# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import math

golden_mean = (math.sqrt(5)-1.0)/2.0       # Aesthetic ratio
fig_width = 3+3/8                          # width  in inches
fig_height = fig_width*golden_mean         # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
          'axes.linewidth': 0.5, 
          'axes.grid': False,
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

###  DATA  ###

data_d2 = np.genfromtxt('speed_profile_w15_density2_fgx4.txt', delimiter = '')
data_d4 = np.genfromtxt('speed_profile_w15_density4_fgx4.txt', delimiter = '')
data_d5 = np.genfromtxt('speed_profile_w15_density5_fgx4.txt', delimiter = '')
data_d6 = np.genfromtxt('speed_profile_w15_density6_fgx4.txt', delimiter = '')
data_d9 = np.genfromtxt('speed_profile_w15_density9_fgx4.txt', delimiter = '')


ancho_d2 = data_d2[:,0] 
v_media_d2 = data_d2[:,1] 
err_media_d2 = data_d2[:,2] 


ancho_d4 = data_d4[:,0] 
v_media_d4 = data_d4[:,1] 
err_media_d4 = data_d4[:,2] 

ancho_d5 = data_d5[:,0] 
v_media_d5 = data_d5[:,1] 
err_media_d5 = data_d5[:,2] 

ancho_d6 = data_d6[:,0] 
v_media_d6 = data_d6[:,1] 
err_media_d6 = data_d6[:,2] 


ancho_d9 = data_d9[:,0] 
v_media_d9 = data_d9[:,1] 
err_media_d9 = data_d9[:,2] 



###  PLOT  ###

pylab.figure(1)
pylab.clf()


plt.plot(ancho_d2[::],v_media_d2[::],'bo',markersize=4,zorder=3,label='$\\rho$=2~p/m$^2$') 
plt.plot(ancho_d2[::],v_media_d2[::],'b',lw=0.6,zorder=2)
plt.errorbar(ancho_d2[::],v_media_d2[::],err_media_d2[::],linestyle='-',fmt='.',color='w',ecolor='b',zorder=1) 


plt.plot(ancho_d4[::],v_media_d4[::],'go',markersize=4,zorder=3,label='$\\rho$=4~p/m$^2$') 
plt.plot(ancho_d4[::],v_media_d4[::],'g',lw=0.6,zorder=2)
plt.errorbar(ancho_d4[::],v_media_d4[::],err_media_d4[::],linestyle='-',fmt='.',color='w',ecolor='g',zorder=1) 


plt.plot(ancho_d5[::],v_media_d5[::],'co',markersize=4,zorder=3,label='$\\rho$=5~p/m$^2$') 
plt.plot(ancho_d5[::],v_media_d5[::],'c',lw=0.6,zorder=2)
plt.errorbar(ancho_d5[::],v_media_d5[::],err_media_d5[::],linestyle='-',fmt='.',color='w',ecolor='c',zorder=1) 


plt.plot(ancho_d6[::],v_media_d6[::],'ro',markersize=4,zorder=3,label='$\\rho$=6~p/m$^2$') 
plt.plot(ancho_d6[::],v_media_d6[::],'r',lw=0.6,zorder=2)
plt.errorbar(ancho_d6[::],v_media_d6[::],err_media_d6[::],linestyle='-',fmt='.',color='w',ecolor='r',zorder=1) 


plt.plot(ancho_d9[::],v_media_d9[::],'ko',markersize=4,zorder=3,label='$\\rho$=9~p/m$^2$') 
plt.plot(ancho_d9[::],v_media_d9[::],'k',lw=0.6,zorder=2)
plt.errorbar(ancho_d9[::],v_media_d9[::],err_media_d9[::],linestyle='-',fmt='.',color='w',ecolor='k',zorder=1) 


pylab.legend()
#pylab.xticks(np.arange(0,9,2))
pylab.yticks(np.arange(0,1.1,0.25))
pylab.xlabel('y position (m)')
pylab.ylabel('velocity (m/s)')
pylab.ylim(0, 1.2)
pylab.xlim(0, 15.2)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(loc='best',labelspacing=0.1,borderpad=0.1,handletextpad=0.1,fontsize=6,numpoints=1)
pylab.savefig('v(y)_width15_fgx4.png', format='png', dpi=300, bbox_inches='tight')
