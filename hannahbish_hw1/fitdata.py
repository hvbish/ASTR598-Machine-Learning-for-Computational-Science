import numpy as np
import matplotlib.pyplot as plt

#Homoscedastic data
x,y = np.loadtxt("data.out", unpack=True)

#Least squares estimation of a and b
a = ((np.mean(x*y))-(np.mean(x)*np.mean(y)))/((np.mean(x*x))-((np.mean(x))**2))
b = np.mean(y) - a*np.mean(x)

print "a = ",a
print "b = ",b

plt.scatter(x,y)
plt.plot(x,(a*x)+b,'r')
plt.title('Homoscedastic Least Squares Fit')
#plt.xlim(np.min(x),np.max(x))
#plt.ylim(np.min(y),np.max(y))
plt.savefig('homofit.png')

plt.show()

plt.scatter(x,y-(a*x)-b)
plt.title('Homoscedastic Least Squares Residuals')
plt.savefig('homoresiduals.png')

plt.show()

#Heteroscedatic Data
x,y = np.loadtxt("data2.out", unpack=True)

#Least squares estimation of a and b
a = ((np.mean(x*y))-(np.mean(x)*np.mean(y)))/((np.mean(x*x))-((np.mean(x))**2))
b = np.mean(y) - a*np.mean(x)

print "a = ",a
print "b = ",b

plt.scatter(x,y)
plt.plot(x,(a*x)+b,'r')
plt.title('Heteroscedastic Least Squares Fit')
#plt.xlim(np.min(x),np.max(x))
#plt.ylim(np.min(y),np.max(y))
plt.savefig('heterofit.png')

plt.show()

plt.scatter(x,y-(a*x)-b)
plt.title('Heteroscedastic Least Squares Residuals')
plt.savefig('heteroresiduals.png')

plt.show()