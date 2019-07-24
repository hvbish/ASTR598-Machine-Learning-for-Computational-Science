import numpy as np

h = 0.1

test = np.genfromtxt('iris.test', dtype=None, names = ['slength','swidth','plength','pwidth','class'])

def kde_setosa(h,slength,swidth,plength,pwidth):
    train_set = np.genfromtxt('iris.setosa', dtype=None, names = ['slength','swidth','plength','pwidth','class'])
    distance = np.sqrt((slength-train_set['slength'][:])**2+(swidth-train_set['swidth'][:])**2+(plength-train_set['plength'][:])**2+(pwidth-train_set['pwidth'][:])**2)    
    #print distance
    K = ((1/(np.sqrt(2*np.pi)*h)**4)*np.exp(-1*((distance)**2)/(2*h**2)))
    runsum = 0.0
    for i in range(len(train_set)):
        runsum = runsum + (K[i]*distance[i])
    return runsum/len(train_set)
    
def kde_versicolor(h,slength,swidth,plength,pwidth):
    train_set = np.genfromtxt('iris.versicolor', dtype=None, names = ['slength','swidth','plength','pwidth','class'])
    distance = np.sqrt((slength-train_set['slength'][:])**2+(swidth-train_set['swidth'][:])**2+(plength-train_set['plength'][:])**2+(pwidth-train_set['pwidth'][:])**2)    
    K = ((1/(np.sqrt(2*np.pi)*h)**4)*np.exp(-1*((distance)**2)/(2*h**2)))
    runsum = 0.0
    for i in range(len(train_set)):
        runsum = runsum + (K[i]*distance[i])
    return runsum/len(train_set)    
    
    
def kde_virginica(h,slength,swidth,plength,pwidth):
    train_set = np.genfromtxt('iris.virginica', dtype=None, names = ['slength','swidth','plength','pwidth','class'])
    distance = np.sqrt((slength-train_set['slength'][:])**2+(swidth-train_set['swidth'][:])**2+(plength-train_set['plength'][:])**2+(pwidth-train_set['pwidth'][:])**2)    
    K = ((1/(np.sqrt(2*np.pi)*h)**4)*np.exp(-1*((distance)**2)/(2*h**2)))
    runsum = 0.0
    for i in range(len(train_set)):
        runsum = runsum + (K[i]*distance[i])
    return runsum/len(train_set)   
    
    
kde_sets = np.zeros(len(test))
kde_vers = np.zeros(len(test))
kde_virs = np.zeros(len(test))

for t in range(len(test)):
    kde_sets[t] = kde_setosa(h,test['slength'][t],test['swidth'][t],test['plength'][t],test['pwidth'][t])
    kde_vers[t] = kde_versicolor(h,test['slength'][t],test['swidth'][t],test['plength'][t],test['pwidth'][t])
    kde_virs[t] = kde_virginica(h,test['slength'][t],test['swidth'][t],test['plength'][t],test['pwidth'][t])

np.savetxt('kde.out',np.transpose([kde_sets, kde_vers, kde_virs, test['class']]),fmt='%-20s',header='Setosa  Versicolor  Virginica  Class')
    
