import numpy as np

N=1000
lowlim=0.
highlim=10.
a=1.
b=2.
mu=0.
c=0.1

x = np.array(np.random.uniform(lowlim, highlim, N))
sigma = c*x
noise = np.array(np.random.normal(mu, sigma))
y = a*x + b + noise
np.savetxt('data2.out',np.transpose([x,y]))