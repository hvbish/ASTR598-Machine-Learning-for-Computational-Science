import numpy as np

filename='iris.train'

train = np.genfromtxt(filename, dtype=None, names = ['slength','swidth','plength','pwidth','class'])


np.savetxt('iris.setosa', train[train['class']=='Iris-setosa'], fmt='%f %f %f %f %s')
np.savetxt('iris.versicolor', train[train['class']=='Iris-versicolor'], fmt='%f %f %f %f %s')
np.savetxt('iris.virginica', train[train['class']=='Iris-virginica'], fmt='%f %f %f %f %s')
