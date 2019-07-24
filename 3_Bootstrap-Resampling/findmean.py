import numpy as np

data = np.loadtxt("data.out", unpack=True)
print np.mean(data)