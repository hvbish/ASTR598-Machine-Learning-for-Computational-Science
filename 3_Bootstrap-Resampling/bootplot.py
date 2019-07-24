import numpy as np
import matplotlib.pyplot as plt


means = np.loadtxt("boot.out", unpack=True)
plt.hist(means)
plt.title(r'$M = $'+str(len(means)),fontsize=20)
plt.xlabel(r'$\mu$',fontsize=15)
plt.ylabel(r'$N$',fontsize=15)

plt.savefig(str(len(means))+'_mean_dist.png')
plt.show()