import numpy as np
import pandas as pd
from astropy.table import Table, Column

iris_dataset = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

iris = np.recfromcsv(iris_dataset, encoding=None)  # in numpy
iris = pd.read_csv(iris_dataset)  # in pandas


