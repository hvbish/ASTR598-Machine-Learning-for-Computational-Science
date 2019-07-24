1. Run maketrain.py, which will read in iris.data and produce iris.train & iris.test
2. Run splittrain.py, which will read in iris.train and produce iris.setosa, iris.versicolor, & iris.virginica
3. Run trykde.py, which will read in the output files from parts 1 & 2 and output kde.out. The bandwidth h can be changed at the top of the file.

(h) For each row in kde.out, the Iris type is the same as that corresponding to the highest KDE value.