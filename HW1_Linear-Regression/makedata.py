import numpy as np
import matplotlib.pyplot as plt

N=1000
lowlim=0.
highlim=10.
a=1.
b=2.
mu=0.
sigma=0.1

x = np.array(np.random.uniform(lowlim, highlim, N))
noise = np.array(np.random.normal(mu, sigma, N))
#print noise
y = a*x + b + noise
np.savetxt('data.out',np.transpose([x,y]))

#plt.hist(noise,10)
#plt.show()
    