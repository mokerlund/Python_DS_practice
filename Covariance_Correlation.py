#Covariance = a measure of how two variables vary in tandem from their means
#Measuring Covariance = think of the data sets for the two variables as high-dimensional vectors,
#convert these to vectors of variances from the mean, take the dot product (cosine of the angle between them)
#of the two vectors, then divide by sample size
#small covariance means that there isn't much correlation (close to 0)
#-1 is perfect inverse correlation, 0 is no correlation, 1 is perfect positive correlation
#Correlation does not mean causation#

import numpy as np
import matplotlib.pyplot as plt

def de_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return np.dot(de_mean   (x), de_mean(y)) / (n-1)

page_speeds = np.random.normal(3, 1, 1000)
purchase_amount = np.random.normal(50, 10, 1000)

plt.scatter(page_speeds, purchase_amount)

covariance(page_speeds, purchase_amount)

purchase_amount = np.random.normal(50, 10, 1000) / page_speeds

plt.scatter(page_speeds, purchase_amount)

covariance(page_speeds, purchase_amount)

def correlation(x, y):
    stddevx = x.std()
    stddevy = x.std()
    return covariance(x,y) / stddevx / stddevy

correlation(page_speeds, purchase_amount)
np.corrcoef(page_speeds, purchase_amount)

purchase_amount= 100 - page_speeds * 3

plt.scatter(page_speeds, purchase_amount)
correlation(page_speeds, purchase_amount)
plt.scatter(page_speeds, purchase_amount)

#Activity
#Use numpy.cov to compute Covariance for you

np.cov(page_speeds, purchase_amount)