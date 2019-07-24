import numpy as np

M = 10000

data = np.loadtxt("data.out", unpack=True)
N = len(data)

means = np.empty(M)
for meannum in range(M):
    resamp = np.empty(N)
    for i in range(N):
        resamp[i] = data[np.random.randint(0,len(data))]
    means[meannum] = np.mean(resamp) 


np.savetxt('boot.out',np.transpose([means])) 

