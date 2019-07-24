import numpy as np

def nearest_neighbor(slength,swidth,plength,pwidth):
    train_set = np.genfromtxt('iris.train', dtype=None, names = ['slength','swidth','plength','pwidth','class'])
    mindist = 9999.
    minindex = len(train_set)
    for i in range(len(train_set)):        
        distance = np.sqrt((slength-train_set['slength'][i])**2+(swidth-train_set['swidth'][i])**2+(plength-train_set['plength'][i])**2+(pwidth-train_set['pwidth'][i])**2)
        if distance < mindist:
            mindist = distance
            minindex = i
    return train_set['class'][minindex]
    

test_set = np.genfromtxt('iris.test', dtype=None, names = ['slength','swidth','plength','pwidth','class'])
nn_class = np.empty(len(test_set),dtype='a20')

for i_test in range(len(test_set)):
    nn_class[i_test] = nearest_neighbor(test_set['slength'][i_test],test_set['swidth'][i_test],test_set['plength'][i_test],test_set['pwidth'][i_test])


np.savetxt('nn.out',np.transpose([nn_class, test_set['class']]),fmt='%-20s',header='Neighbor Type      Real Type')