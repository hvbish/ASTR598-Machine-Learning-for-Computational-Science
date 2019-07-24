import numpy as np

def nearest_neighbor3(slength,swidth,plength,pwidth):
    train_set = np.genfromtxt('iris.train', dtype=None, names = ['slength','swidth','plength','pwidth','class'])
    neardist = 9999.
    meddist = 9999.
    fardist = 9999.
    nearindex = len(train_set)
    medindex = len(train_set)
    farindex = len(train_set)
    for i in range(len(train_set)):        
        distance = np.sqrt((slength-train_set['slength'][i])**2+(swidth-train_set['swidth'][i])**2+(plength-train_set['plength'][i])**2+(pwidth-train_set['pwidth'][i])**2)
        if distance < neardist:
            fardist = meddist
            farindex = medindex
            meddist = neardist
            medindex = nearindex
            neardist = distance
            nearindex = i
        elif distance < meddist:
            fardist = meddist
            farindex = medindex
            meddist = distance
            medindex = i
        elif distance <  fardist:
            fardist = distance
            farindex = i
    #print neardist,meddist,fardist
    return train_set['class'][nearindex],train_set['class'][medindex],train_set['class'][farindex]
    


test_set = np.genfromtxt('iris.test', dtype=None, names = ['slength','swidth','plength','pwidth','class'])
nn3_nearclass = np.empty(len(test_set),dtype='a20')
nn3_medclass = np.empty(len(test_set),dtype='a20')
nn3_farclass = np.empty(len(test_set),dtype='a20')

for i_test in range(len(test_set)):
    nn3_nearclass[i_test], nn3_medclass[i_test], nn3_farclass[i_test] = nearest_neighbor3(test_set['slength'][i_test],test_set['swidth'][i_test],test_set['plength'][i_test],test_set['pwidth'][i_test])
    
np.savetxt('nn3.out',np.transpose([nn3_nearclass, nn3_medclass, nn3_farclass, test_set['class']]),fmt='%-20s',header='Neighbor 1 Type    Neighbor 2 Type      Neighbor 3 Type      Real Type')