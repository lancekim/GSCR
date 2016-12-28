# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 10:03:13 2015

@author: kimlanc
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy

# Flow as function of reactor power and deltaT
def power(DT,Vdot,rho=1000,cp=4200):
    # Power [MWt], DT [degC or K], Vdot [m3/day], rho [kg/m3], cp [J/kgK]
    Vdot=Vdot/86400 # [m3/s]    
    Q=(Vdot*rho*cp*DT)/1E6
    return Q 


    
DT= numpy.linspace(10, 100, 100) # degC or K    
Vdot = numpy.linspace(0, 70000, 100) # m3/day
X,Y = numpy.meshgrid(DT, Vdot)
rho = 1000 # kg/m3
cp = 4200 # J/kgK
Q = power(X, Y,rho,cp)
#fig, ax = plt.subplots()
#cnt = plt.contour(Q, cmap=plt.cm.RdBu, vmin=abs(Q).min(), vmax=abs(Q).max())
plt.figure(figsize=[5.5,5.5])
plevels=[10,30]
CS=plt.contour(X,Y,Q,plevels,colors='k')
#CS=plt.contour(X,Y,Q,colors='k')
manual_locations = [(22, 10000), (35, 21000)]
matplotlib.rcParams['mathtext.fontset']='cm'
matplotlib.rcParams['mathtext.default']='regular'
plt.xlim( (10,80) )
plt.ylim( (0,60000) )
plt.clabel(CS,inline=1,fontsize=12,fmt='%1i MWt',manual=manual_locations)
plt.title('Cooling Water Flow', fontsize=12)
plt.xlabel(r'$\Delta$T [$^\bigcirc$C or K]',fontsize=12)
plt.ylabel(r'Flow [m$^3$/day]',fontsize=12)
plt.savefig('power.tif',dpi=600., bbox_inches='tight')



def breakthrough(L,DT,K,b,I,rho=1000.,cp=4200.):
    # Power[MWt], L[m], DT[degC or K], K[m/s],I[0-1],rho[kg/m3],cp[J/kgK]
    Q=1e-6*(0.5*L*K*b*numpy.pi*I*rho*cp*DT)
    return Q
    
DT= numpy.linspace(0, 100, 100) # degC or K    
L = numpy.linspace(0,10000,100)
K=0.001 #[m/s]
b=1 #[m] (Kb=0.001m2/s)
I=0.01 #[]
L,DT = numpy.meshgrid(L,DT)
Q = breakthrough(L,DT,K,b,I)
#fig, ax = plt.subplots()
#cnt = plt.contour(Q, cmap=plt.cm.RdBu, vmin=abs(Q).min(), vmax=abs(Q).max())
fig=plt.figure(figsize=[5.5,5.5])
fig.subplots_adjust(wspace=0.3,hspace=0.3)
plevels=[10,30]

plt.suptitle('Minimum Doublet Separation', fontsize=12)


ax=plt.subplot(2,2,1)
CS=plt.contour(DT,L,Q,plevels,colors='k')
#CS=plt.contour(X,Y,Q,colors='k')
matplotlib.rcParams['mathtext.fontset']='cm'
matplotlib.rcParams['mathtext.default']='regular'
plt.xlim( (10,80) )
plt.ylim( (0,10000) )
#plt.clabel(CS,inline=1,fontsize=10,fmt='%1i MWt')
manual_locations = [(20, 100), (60,7000)]
plt.clabel(CS,inline=1,fontsize=10,fmt='%1i MWt',manual=manual_locations)
plt.xlabel(r'$\Delta$T [$^\bigcirc$C or K]',fontsize=10)
plt.ylabel(r'Separation [m]',fontsize=10)
ax.annotate('Kb=0.001m$^{2}/s$\n I=0.01',xy=(0.05,0.05),xycoords='axes fraction',fontsize=10,
          horizontalalignment='left',verticalalignment='bottom')

K = 0.001 #[m/s] (Kb=0.001m2/s)
b = 1 #[m] (Kb=0.001m2/s)
DT = 70 # [degC]
I = numpy.linspace(0.001,0.15,100) #[]
L = numpy.linspace(0,7000,100)
L,I = numpy.meshgrid(L,I)
Q = breakthrough(L,DT,K,b,I)
#fig, ax = plt.subplots()
#cnt = plt.contour(Q, cmap=plt.cm.RdBu, vmin=abs(Q).min(), vmax=abs(Q).max())
ax=plt.subplot(2,2,2)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(numpy.arange(start, end, 0.05))
CS=plt.contour(I,L,Q,plevels,colors='k')
plt.ylim( (0,5000) )
plt.xlim( (0.00,0.15))
#CS=plt.contour(X,Y,Q,colors='k')
#manual_locations = [(42, 4200), (54, 6000), (65, 8000)]
matplotlib.rcParams['mathtext.fontset']='cm'
matplotlib.rcParams['mathtext.default']='regular'
manual_locations = [(0.03,500), (0.05,1000)]
plt.clabel(CS,inline=1,fontsize=10,fmt='%1i MWt',manual=manual_locations)
plt.xlabel('Hydraulic Gradient, I',fontsize=10)
#plt.ylabel(r'Doublet Separation [m]',fontsize=12)
#plt.ylabel(r'Separation [m]',fontsize=10)
ax.annotate('Kb=0.001$m^{2}/s$',xy=(0.9,0.9),xycoords='axes fraction',fontsize=10,
          horizontalalignment='right',verticalalignment='top')
ax.annotate(r'$\Delta$T=70',xy=(0.9,0.8),xycoords='axes fraction',fontsize=10,
          horizontalalignment='right',verticalalignment='top')

K = numpy.logspace(-6,-3,100) #[m/s]
b = 50 #[m]
DT = 70 # [degC]
I = 0.15 #[]
L = numpy.linspace(0,7000,100)
L,K = numpy.meshgrid(L,K)
Q = breakthrough(L,DT,K,b,I)
#fig, ax = plt.subplots()
#cnt = plt.contour(Q, cmap=plt.cm.RdBu, vmin=abs(Q).min(), vmax=abs(Q).max())
ax=plt.subplot(2,2,3)
CS=plt.contour(K,L,Q,plevels,colors='k')
ax.set_xscale('log')
plt.ylim( (10,1000) )
ax.set_yscale('log')
#CS=plt.contour(X,Y,Q,colors='k')
matplotlib.rcParams['mathtext.fontset']='cm'
matplotlib.rcParams['mathtext.default']='regular'
manual_locations = [(2e-5, 80), (9E-5,200)]
plt.clabel(CS,inline=1,fontsize=10,fmt='%1i MWt',manual=manual_locations)
plt.xlabel('Hydraulic Conductivity, K [m/s]',fontsize=10)
plt.ylabel(r'Separation [m]',fontsize=10)
ax.annotate('I=0.15\nb=50m',xy=(0.9,0.9),xycoords='axes fraction',fontsize=10,
          horizontalalignment='right',verticalalignment='top')
ax.annotate(r'$\Delta$T=70',xy=(0.9,0.74),xycoords='axes fraction',fontsize=10,
          horizontalalignment='right',verticalalignment='top')

ax=plt.subplot(2,2,4)
K=1E-5 #[m/s]
b = numpy.linspace(0,100,100) #[m]
DT=70 # [degC]
I=0.15 #[]
L = numpy.linspace(0,2000,100)
L,b = numpy.meshgrid(L,b)
Q = breakthrough(L,DT,K,b,I)
#fig, ax = plt.subplots()
#cnt = plt.contour(Q, cmap=plt.cm.RdBu, vmin=abs(Q).min(), vmax=abs(Q).max())
CS=plt.contour(b,L,Q,plevels,colors='k')
plt.xlim( (0,100))
plt.ylim( (0,1000) )
#CS=plt.contour(X,Y,Q,colors='k')
#manual_locations = [(42, 4200), (54, 6000), (65, 8000)]
matplotlib.rcParams['mathtext.fontset']='cm'
matplotlib.rcParams['mathtext.default']='regular'
manual_locations = [(40, 400), (60,600)]
plt.clabel(CS,inline=1,fontsize=10,fmt='%1i MWt',manual=manual_locations)
#plt.clabel(CS,inline=1,fontsize=12,fmt='%1i MWt',manual=manual_locations)
plt.xlabel('Aquifer Thickness, b [m]',fontsize=10)
ax.annotate('K=1e-5m/s\nI=0.15',xy=(0.05,0.13),xycoords='axes fraction',fontsize=10,
          horizontalalignment='left',verticalalignment='bottom')
ax.annotate(r'$\Delta$T=70',xy=(0.04,0.05),xycoords='axes fraction',fontsize=10,
          horizontalalignment='left',verticalalignment='bottom')

plt.savefig('separation.tif',dpi=600., bbox_inches='tight')


plt.figure(figsize=[5.5,5.5])
K=numpy.array([[1.00E-03,1.00E+00],
               [2.00E-06, 1.00E-02],
               [1.00E-06, 1.00E-02],
               [1.00E-07,1.00E-02],
               [1.00E-07,1.00E-03],
               [1.00E-08,1.00E-04],
               [1.00E-09,2.00E-06],
               [1.00E-10,1.00E-06],
               [1.50E-12,1.00E-06],
               [8.00E-13,1.00E-09],
               [1.00E-13,8.00E-10],
               [7.00E-14,1.00E-10]])
   
labels=('Gravel','Clean Sand','Karst Limestone','Transmissive\nBasalt',
        'Silty Sand','Fractured\nCrystalline Rock','Limestone\nDolomite',
        'Sandstone','Glacial Till','Unweathered\nMarine Clay','Shale',
        'Unfractured\nCrystalline Rock')
        
ind=numpy.arange(len(K))+0.2
left=K[:,0]
width=K[:,1]-K[:,0]
height=0.5
#p2=plt.barh(ind,K[:,1], width, color='r',log=1)
#p1=plt.barh(ind,K[:,0], width, edgecolor='w',color='w',log=1)
p1=plt.barh(ind,width,height,left,log=1,color='w')
plt.xlabel('Hydraulic Conductivity, K [m/s]',fontsize=12)
plt.title('Hydraulic Conductivity of Geologic Media',fontsize=12)
plt.yticks(ind+height/2.,labels,fontsize=12)
plt.xlim(1E-14,10)
plt.savefig('K.tif',dpi=600., bbox_inches='tight')       


def evap(hvap,P0,t,t0):
    # hvap [MJ/kg], P0 [MWt], t [sec]
    m = (0.0825 * P0 * ( t**0.8 - (t+t0)**0.8 + t0**0.8))/hvap
    return m
    
plt.figure(figsize=[5.5,5.5])
P0=30 #[MWt]
t0=3.15E7 #[sec]
t=numpy.logspace(1,9,100) #[sec]
m=evap(2.26,P0,t,t0)
V=m/1000 # convert kg to m3
ax=plt.loglog(t/86400,V,color='k') # convert seconds to days
plt.xlim(1e-4,100)
#plt.ylim(0,1e3)
plt.xlabel('Time After Shutdown, t [days]',fontsize=12)
plt.ylabel(r'Water (Cumulative) [m$^3$]',fontsize=12)
plt.title('Evaporative Losses of\nEmergency Core Cooling Water',
          fontsize=12)
plt.annotate('Po=30MWt\nto=1year',xy=(0.95,0.95),xycoords='axes fraction',
             fontsize=12, horizontalalignment='right',verticalalignment='top')
plt.savefig('evap.tif',dpi=600., bbox_inches='tight') 
#ax.set_xscale('log')
#ax.set_xscale('log')