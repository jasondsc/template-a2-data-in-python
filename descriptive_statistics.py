import numpy as np
import pandas as pd
from astropy.table import Table, Column

iris_dataset = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

iris = np.recfromcsv(iris_dataset, encoding=None)  # in numpy
iris = pd.read_csv(iris_dataset)  # in pandas

setosa=iris[iris.species=='setosa']
versicolor=iris[iris.species=='versicolor']
verginica=iris[iris.species=='virginica']

m_setosa=np.mean(setosa.sepal_length)
m_versicolor=np.mean(versicolor.sepal_length)
m_verginica=np.mean(verginica.sepal_length)
 
sd_setosa=np.std(setosa.sepal_length)
sd_versicolor=np.std(versicolor.sepal_length)
sd_verginica=np.std(verginica.sepal_length)
 
t= Table() 
t['Iris Type']= ['Setosa', 'Versicolor', 'Virginica']
t['Mean Sepal Length']= [m_setosa, m_versicolor, m_verginica]
t['Standard Deviation Sepal Length']= [sd_setosa, sd_versicolor, sd_verginica]

t
