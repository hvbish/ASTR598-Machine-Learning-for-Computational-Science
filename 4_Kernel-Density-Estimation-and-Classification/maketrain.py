import numpy as np

filename='iris.data'

#Read in data
data = np.genfromtxt(filename, dtype=None, names = ['slength','swidth','plength','pwidth','class'], delimiter=",")

#Generate test set randomly from data, then remove those elements from data
test_i = np.random.choice(range(len(data)),size=10,replace=False)
test = data[test_i]
train = np.delete(data,test_i)

print data[0:10]['class']
print test['slength']

np.savetxt('iris.train', train, fmt='%f %f %f %f %s')
np.savetxt('iris.test', test, fmt='%f %f %f %f %s')
