# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:41:39 2016

@author: lancekim
"""

#import matplotlib
import matplotlib.pyplot as plt
import numpy
from cycler import cycler
##################################
# Drawndown Curve (Steady state) 
# Thiem equation
# Unconfined aquifer
##################################
def head(ho,Q,K,ro,r):
    # Head at well casing ho [m], Pumping Rate Q[m3/s], 
    # Hydraulic Conductivity K[m/s], Well casing radius, ro[m]
    # Radius, r [m] (r>r0) 
    h=numpy.sqrt( ho**2 + (Q/(numpy.pi*K)) * numpy.log10(r/ro) )
    return h 

K=[1E-6,1E-5,1E-4,1E-3]
plt.figure(figsize=[5.5,5.5])
for K in K:
    ho=0
    Q=0.1 #[m**3/s]
    #K=1E-4 #[m/s]
    ro=0.25 # [m]   
    r=numpy.linspace(ro, 500, 1000)
    h=head(ho,Q,K,ro,r)

    ax=plt.plot(r,h,color='k') # convert seconds to days
    

plt.xlabel('Radius [m]',fontsize=12)
plt.ylabel('Head [m]',fontsize=12)
plt.title('Well Drawdown\nUnconfined Aquifer',
          fontsize=12)
plt.annotate('r0=0.25m',xy=(0.05,0.965),xycoords='axes fraction',
             fontsize=12, horizontalalignment='left',verticalalignment='top')
plt.annotate('K=1E-6m/s',xy=(0.95,0.965),xycoords='axes fraction',
             fontsize=12, horizontalalignment='right',verticalalignment='top')
plt.annotate('K=1E-5m/s',xy=(0.95,0.33),xycoords='axes fraction',
             fontsize=12, horizontalalignment='right',verticalalignment='top')
plt.annotate('K=1E-4m/s',xy=(0.95,0.135),xycoords='axes fraction',
             fontsize=12, horizontalalignment='right',verticalalignment='top')
plt.annotate('K=1E-3m/s',xy=(0.95,0.07),xycoords='axes fraction',
             fontsize=12, horizontalalignment='right',verticalalignment='top')
plt.savefig('drawdown.tif',dpi=600., bbox_inches='tight') 

###############################
# Drawndown Curve (Transient)
# Theis equation
# Confined aquifer
###############################
from scipy import special

# Well Function
def well_func(u):
    # Approximation for exponential integral
    #w=-0.577215664-numpy.log(u) # Gamma is the Euler-Mascheroni constant
    # Exponential integral
    w=special.expn(1,u)    
    return w

# Theis' Equation
def head_theis(Q,K,b,S,r,t):
    u=0.25*S*(r**2)/(K*b*t)
    s=(0.25*Q/(numpy.pi*K*b))*well_func(u)
    return s

# Drawdown Curve
time = numpy.array([10,100,1000]) #days
timesteps=time * 86400 #s

r=numpy.linspace(0.25,2000,100)
Q=0.103#m**3/s
K=1E-6 #m/s
b=50 #m
S=5E-3 # Storativity

plt.figure(figsize=[5.5,5.5])
ax=plt.subplot(2,1,1)
plt.xlim(0,2000)
plt.ylim(0,1000)
plt.gca().invert_yaxis()
plt.suptitle('Cone of Depression, Confined Aquifer\n$\mathregular{Q=8900m^3/d}$, $\mathregular{b=50m}$, $\mathregular{S=5X10^{-3}}$', fontsize=12)

for t in timesteps:
    h=head_theis(Q,K,b,S,r,t)
    plt.rc('axes', prop_cycle=(cycler('linestyle', ['-', '--', ':', '-.'])))
    plt.plot(r,h,color='k')

plt.ylabel('Drawdown [m]',fontsize=12)
#plt.legend(['$\mathregular{10^4 s}$','$\mathregular{10^6 s}$','$\mathregular{10^8 s}$'],bbox_to_anchor=(1,0),loc='lower right')
#ax.annotate('$\mathregular{Q=8900m^3/d}$\n$\mathregular{b=50m}$\n$\mathregular{S=0.14}$\n$\mathregular{K=10^{-6} m/s}$',xy=(0.05,0.05),xycoords='axes fraction',fontsize=12,
#          horizontalalignment='left',verticalalignment='bottom')
ax.annotate('$\mathregular{K=10^{-6} m/s}$',xy=(0.05,0.05),xycoords='axes fraction',fontsize=12,
          horizontalalignment='left',verticalalignment='bottom')
plt.legend(['10 days','100 days','1000 days'],bbox_to_anchor=(1,0),loc='lower right')

K=1E-4 #m/s
r=numpy.linspace(0.25,100,100)

ax=plt.subplot(2,1,2)
plt.xlim(0,100)
plt.ylim(0,50)
plt.gca().invert_yaxis()

for t in timesteps:
    h=head_theis(Q,K,b,S,r,t)
    plt.rc('axes', prop_cycle=(cycler('linestyle', ['-', '--', ':', '-.'])))
    plt.plot(r,h,color='k')
    
plt.ylabel('Drawdown [m]',fontsize=12,labelpad=17)
ax.annotate('$\mathregular{K=10^{-4} m/s}$',xy=(0.05,0.05),xycoords='axes fraction',fontsize=12,
          horizontalalignment='left',verticalalignment='bottom')
plt.legend(['10 days','100 days','1000 days'],bbox_to_anchor=(1,0),loc='lower right')
plt.xlabel('Radius [m]',fontsize=12)
#plt.legend(['$\mathregular{10^4 s}$','$\mathregular{10^6 s}$','$\mathregular{10^8 s}$'],bbox_to_anchor=(1,0),loc='lower right')
plt.savefig('drawdownsurface.tif',dpi=600., bbox_inches='tight') 
plt.close


# Drawdown over time
t=numpy.logspace(-5,8,100) # timesteps in seconds
t_days=t/86400 # timesteps in days

r=0.25 #m
Q=0.103 #m**3/s
b=50 #m
Kspace=[1E-6,1E-5,1E-4]

plt.figure(figsize=[5.5,5.5])
ax=plt.subplot(2,1,1)
plt.xlim(1E-10,1e3)
plt.ylim(1E-3,1E4)
plt.ylabel('Drawdown (r=0.25m) [m]',fontsize=12)

for K in Kspace:
    h=head_theis(Q,K,b,S,r,t)
    plt.rc('axes', prop_cycle=(cycler('linestyle', ['-', '--', ':', '-.'])))
    plt.loglog(t_days,h,color='k')

plt.annotate('$\mathregular{S=5X10^{-3}}$',\
            xy=(0.02,0.95),xycoords='axes fraction',fontsize=12,\
            horizontalalignment='left',verticalalignment='top')

# Reduce storativity
S=0.01*S
ax=plt.subplot(2,1,2)

for K in Kspace:
    h=head_theis(Q,K,b,S,r,t)
    plt.rc('axes', prop_cycle=(cycler('linestyle', ['-', '--', ':', '-.'])))
    plt.loglog(t_days,h,color='k')

plt.xlim(1E-10,1e3)
plt.ylim(1E-3,1E4)
plt.xlabel('Pumping Time [days]',fontsize=12)
plt.ylabel('Drawdown (r=0.25m) [m]',fontsize=12)
plt.annotate('$\mathregular{S=5X10^{-5}}$',\
            xy=(0.02,0.95),xycoords='axes fraction',fontsize=12,\
            horizontalalignment='left',verticalalignment='top')
plt.suptitle('Well Drawdown, Confined Aquifer\n$\mathregular{Q=8900m^3/d}$, $\mathregular{b=50m}$',fontsize=12)
plt.legend(['$\mathregular{K=10^{-6} m/s}$','$\mathregular{K=10^{-5} m/s}$',\
            '$\mathregular{K=10^{-4} m/s}$'], bbox_to_anchor=(1,0),loc='lower right',\
            fontsize=12)
plt.savefig('drawdowntime.tif',dpi=600., bbox_inches='tight') 