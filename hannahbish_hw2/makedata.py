import numpy as np
import matplotlib.pyplot as plt

N = 1000
beta_0 = 2
beta_1 = 3
L = 50



# 1: Generate N uniformly distributed random numbers x between -L and L
x = np.random.uniform(-L,L,N)

# 2: Compute N values of p
p = 1/(1+np.exp(-1*(beta_0+(beta_1*x[:]))))

# 3: Compute N values of y where y is a binomial random variable which is 1 with probability p and 0 with probability 1-p
# To do this I will create an array y with c*p elements equaling 1 and 1-c*p elements equaling 0
probsampsize = 10000
y = np.empty(N)
probarray = np.empty(probsampsize)
for p_index,probability in enumerate(p): #For each probability corresponding to an x value
    numones = int(round(probability*probsampsize))
    for i in range(len(probarray)): #Create an array with 1s and 0s occuring with that same probability
        if i<numones:
            probarray[i] = 1
        else:
            probarray[i] = 0
    yval = probarray[np.random.randint(len(probarray))] #Sample that array randomly
    y[p_index] = yval #Assign sampled value to y
    
#print "x = ",x
#print "y = ",y

# 4b: Plot the data
plt.scatter(x,y,color='k',marker='.',s=0.1)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('yvsx.png')

plt.xlim(-5,5)
plt.savefig('yvsx_zoom')

np.savetxt('data.out',np.transpose([x,y]))

# 4d: "back of the envelope" approximation
delta_x = np.max(x[y==0])-np.min(x[y==1])
print "Width of region over which the function rises from 0 to 1: ", delta_x
beta_1_est = 1/(np.max(x[y==0])-np.min(x[y==1]))
print "Beta_1 = ", beta_1_est
x_0 = (np.max(x[y==0])+np.min(x[y==1]))/2
print "x(p=0.5) = ", x_0
beta_0_est = -1 * beta_1_est * x_0
print "Beta_0 = ", beta_0_est

