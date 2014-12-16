import numpy as np


def evolve_state():
    ar = np.random.randn(10,10,4) # Air,Fuel, Prod1, Prod2
    cp = np.random.randn(10,10)
    hf = np.random.randn(10,10)
    T  = np.random.randn(10,10)*1000
    for i in range(10):
        for j in range(10):
            if T > 300 and ar[i][j][0] > 0.1:
                omega = ar[i][j][0]*ar[i][j][1]*A*np.exp(10000/T[i][j])
                ar[i][j][0] -= omega * s1 * ar[i][j][0]
                ar[i][j][1] -= omega * s2 * ar[i][j][1]
                ar[i][j][2] += omega * s3 * ar[i][j][0]
                ar[i][j][3] += omega * s4 * ar[i][j][1]
                T[i][j] += omega * cp[i][j]* hf[i][j] 
                sum = 0.0
                for k in range(len(ar[i][j])):
                    if ar[i][j][k] < 0.0:
                         ar[i][j][k] = 0.0
                    sum += ar[i][j][k]
                ar[i][j][0] = ar[i][j][0]/sum 
                ar[i][j][1] = ar[i][j][1]/sum 
                ar[i][j][2] = ar[i][j][2]/sum 
                ar[i][j][3] = ar[i][j][3]/sum 


def reaction_k(A,Ta,T):
    return A*np.exp(Ta/T)

def omega(Prod, A, Ta, T):
    return Prod*reaction_k(A,Ta,T)

def reacting_cells(ar_, cp_, hf_, T_):
    for ari, Ti, cpi in zip(ar_, T_, cp_):
        for spec, T, cp in zip(ari, Ti, cpi):
            if T > 300 and spec[0] > 0.1:
                yield spec[0], spec[1], spec[2], spec[3], T, cp


def evolve_state_1():

    ar = np.random.randn(10,10,4) # Air,Fuel, Prod1, Prod2
    cp = np.random.randn(10,10)
    hf = np.random.randn(10,10)
    T  = np.random.randn(10,10)*1000

    for Air, Fuel, Prod1, Prod2, T, cp in reacting_cells(ar, cp, hf, T): 
        omeg = omega(air*fuel, A=10000,Ta=20000, T=T)
        air   -= omeg * s1 * prod 
        fuel  -= omeg * s2 * prod
        prod1 += omeg * s3 * prod
        prod2 += omeg * s4 * prod
        T     += omega * cp* hf
        sum = 0.0
        for k in range(len(ar[i][j])):
            if ar[i][j][k] < 0.0:
                 ar[i][j][k] = 0.0
            sum += ar[i][j][k]
        ar[i][j][0] = ar[i][j][0]/sum 
        ar[i][j][1] = ar[i][j][1]/sum 
        ar[i][j][2] = ar[i][j][2]/sum 
        ar[i][j][3] = ar[i][j][3]/sum 

