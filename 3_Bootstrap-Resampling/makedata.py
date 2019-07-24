import numpy as np

N=1000
mu=0.
sigma=1.

data = np.array(np.random.normal(mu, sigma, N))

#plt.hist(data)

np.savetxt('data.out',np.transpose([data]))