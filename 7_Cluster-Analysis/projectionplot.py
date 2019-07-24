import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('iris.data', dtype=None, names = ['slength','swidth','plength','pwidth','class'], delimiter=",")
setosa = data[np.where(data['class'] == 'Iris-setosa')]
versicolor = data[np.where(data['class'] == 'Iris-versicolor')]
virginica = data[np.where(data['class'] == 'Iris-virginica')]


plt.scatter(setosa['pwidth'],setosa['plength'],color='coral',label='Setosa')
plt.scatter(versicolor['pwidth'],versicolor['plength'],color='darkturquoise',label='Versicolor')
plt.scatter(virginica['pwidth'],virginica['plength'],color='plum',label='Virginica')
plt.xlabel('Petal Width')
plt.ylabel('Petal Length')
plt.title('Iris Dataset Projection Plot')
plt.legend(frameon=False,loc=2)


plt.savefig('projectionplot.pdf')
plt.show()