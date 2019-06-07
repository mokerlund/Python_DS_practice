# Mean Median Mode Practice
##Tutorial##

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

incomes = np.random.normal(27000, 15000, 10000)

plt.hist(incomes, 50)
plt.show()

#Original mean and median
np.mean(incomes)
np.median(incomes)

#What happens to the dataset when you add an outlier
incomes = np.append(incomes, [1000000000])

np.median(incomes)
incomes.mean()

#Mode
ages = np.random.randint(18, high=90, size=500)
ages

stats.mode(ages)

##Exercise - Find Mean, Median, Mode##
incomes = np.random.normal(100.0, 20.0, 10000)
plt.hist(incomes, 50)

incomes.mean()
np.median(incomes)
stats.mode(incomes)

#Standard deviation
incomes.std()