import numpy as np

ngridvals = 2000


# 4c: Write a function likelihood(bet0,beta1)
def likelihood(x,y,beta_0,beta_1):
    N = len(x)
    p = 1/(1+np.exp(-1*(beta_0+(beta_1*x[:]))))
    L_0 = 1.
    L_1 = 1.
    for i in range(N):
        if y[i] == 1.:
            L_1 = L_1*p[i]
        elif y[i] == 0.:
            L_0 = L_0*(1-p[i])
    return L_0*L_1

#print likelihood(x,y,beta_0,beta_1)

#Load x and y values generated by makedata.py
x,y = np.loadtxt("data.out", unpack=True)

# Create a grid of values for beta_0 and beta_1
beta_0 = np.linspace(-10.,10.,ngridvals)
beta_1 = np.linspace(-10.,10.,ngridvals)

# Find values of beta_0 and beta_1 that maximize the likelihood
maxL = 0.
max_b0 = 99
max_b1 = 99
for i,b0 in enumerate(beta_0):
    for j,b1 in enumerate(beta_1):
        if likelihood(x,y,b0,b1) > maxL:
            maxL = likelihood(x,y,b0,b1)
            max_b0 = b0
            max_b1 = b1
            
print "Number of values in grid: ", ngridvals
print "Maximum likelihood beta_0 = ", max_b0
print "Maximum likelihood beta_1 = ", max_b1

