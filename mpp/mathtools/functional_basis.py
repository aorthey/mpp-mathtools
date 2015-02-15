import numpy as np
from math import sin,cos,pi,sqrt
import sys

def Fpoly(x): 
        N=2000
        return np.array(map(lambda e: map(lambda x: pow(x,e), x),np.arange(0,N)))

def Ffourier(x): 
        N = 2000
        ##sqrt(2)*sin(2*pi*N*x)|N\in |N} \cup sqrt(2)*cos(2*pi*N*x) \cup 1
        Fsin = map(lambda N: map(lambda x: sqrt(2)*sin(2*pi*N*x),x),np.arange(0,N))
        Fcos = map(lambda N: map(lambda x: sqrt(2)*cos(2*pi*N*x),x),np.arange(0,N))
        Fone = pow(x,0)
        F = np.vstack((Fsin,Fcos,Fone))
        #print N,len(x),F.shape
        return F


def Flin(x):
        return np.array((pow(x,0),pow(x,1)))

