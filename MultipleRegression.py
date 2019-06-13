#Used for more than one variable that you are ijnterested in
#But if it's multiple dependent variables, it's called multivariate regression
#we get coefficients for each factor- which implies how important each factor is
#must assume they areindependent for this to work

import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

df = pd.read_excel('C://fakepath.exel')

df1=df[['Mileage', 'price']]
bins = np.arange(0, 50000, 10000)
groups = df1.groupby(pd.cut(df['Mileage'], bins)).mean()
print(groups.head())
groups['Price'].plot.line()

scale = StandardScaler()

x = df[[df'Milage', 'Cylinder', 'Doors']]
y = df['Price']

X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].as_matrix())