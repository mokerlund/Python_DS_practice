#Percentiles and Moments

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

np.percentile(vals, 50)
np.percentile(vals, 90)
np.percentile(vals, 20)


#Moments: The ways to measure the shape of a distribution
#1st moment: Mean
#2nd moment: Variance
#3rd moment: skew
#4th moment: kurtosis (how thick is the tail and how sharp is the peak)

np.mean(vals)
np.var(vals)

sp.skew(vals)

sp.kurtosis(vals)