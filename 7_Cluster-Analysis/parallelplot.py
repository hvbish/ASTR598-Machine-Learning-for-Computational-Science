import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import parallel_coordinates

data = pd.read_csv('iris.data')
plt.figure(figsize=(9,6))
parallel_coordinates(data,'class')
plt.savefig('parallelplot.pdf')