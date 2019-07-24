# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 11:43:17 2017

@author: hvbish
"""

import numpy as np
import matplotlib.pyplot as plt


#Choose k
k = 5

#Load data
x,y = np.loadtxt("data.out", unpack=True)

#Choose unique random data points to divide entire training set into k subsets
rand_indices = np.random.choice(len(x),len(x),replace=False)

#Do calculation using each subset as the test set
subset_length = len(x)/k
test_MSE = np.empty(k)
for i in range(k):
    #Create test set
    test_indices = rand_indices[i*subset_length:(i*subset_length)+subset_length]
    #Training set is all points not in test set
    mask_array = np.ones(len(rand_indices),dtype=bool)
    mask_array[test_indices] = False
    train_indices = rand_indices[mask_array]
    
    #Compute least squares estimation of a and b for the training set
    x_train = x[train_indices]
    y_train = y[train_indices]
    a = ((np.mean(x_train*y_train))-(np.mean(x_train)*np.mean(y_train)))/((np.mean(x_train*x_train))-((np.mean(x_train))**2))
    b = np.mean(y_train) - a*np.mean(x_train)

    #Compute test set mean square error
    x_test = x[test_indices]
    y_test = y[test_indices]
    test_MSE[i] = np.sum((((a*x_test)+b)-(y_test))**2)/subset_length
    
avg_MSE = np.mean(test_MSE)

np.savetxt('crossvalidate5.out',[avg_MSE],fmt='%-6.6f')




"""
#Estimate of a and b parameters from HW1 part d
x,y = np.loadtxt("data.out", unpack=True)
#Least squares estimation of a and b
a = ((np.mean(x*y))-(np.mean(x)*np.mean(y)))/((np.mean(x*x))-((np.mean(x))**2))
b = np.mean(y) - a*np.mean(x)

print "a = ",a
print "b = ",b
"""