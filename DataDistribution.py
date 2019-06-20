#Types of Data Distribution
##Uniform Distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson

values= np.random.uniform(-10, 10, 100000)
plt.plot(values)

##Normal/ Gaussian Distribution

x = np.arange(-3, 3, 0.0001)
plt.plot(x, norm.pdf(x))

#Generate some random numbers with a normal distribution. 
#"mu" is the desired mean, "sigma" is the standard deviation

mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)


##Exponential PDF / "Power Law"
x = np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))

##Binomial Probability Mass Function


n,p = 10, .5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))

##Poisson Probability Mass Function
#Shows probability of getting a certain value

#Example: a website gets an avg of 500 views/day, what is the probablility that it would get 550?

mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))

#Quiz#  What is the equivalent of a probability function when using discrete instead of continuous data?
#My Answer# A binomial probability mass function
#Half correct# -- Probability mass function (of any kind)