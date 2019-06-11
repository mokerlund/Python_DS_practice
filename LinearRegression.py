#Sometimes called "Maximum likelihood estimation"
#Can be done with least squares or gradient descent, among other ways

#Measuring error with r-squared ("coefficient of determination")
#measures the fraction of total variation in Y that is captured by the model

#Computing R-Squared: 1.0 - (sum of squared errors) / (sum of squared variation from the mean)
#Interpreting R-Squared: 0 is a bad fit, 1 is a good fit

#Fabricating data that shows a linear relationship between page speed and amnt purchaced
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

page_speeds = np.random.normal(3, 1, 1000)
purchase_amount = 100 - (page_speeds + np.random.normal(0, 0.1, 1000)) * 3

plt.scatter(page_speeds, purchase_amount)

#generate r, p, and std_err values
slope, intercept, r_value, p_value, std_err = stats.linregress(page_speeds, purchase_amount)

#r_squared value shows a good fit bc data is linear anyways
r_value ** 2

#Using slope and intercept to plot predicted vs observed data:
def predict(x):
    return slope * x + intercept

fit_line = predict(page_speeds)

plt.scatter(page_speeds, purchase_amount)
plt.plot(page_speeds, fit_line, c='r')

#Activity: try increasing random variation in the test data to see the effect on r_squared error

page_speeds = np.random.normal(3, .5, 1000)
purchase_amount = 100 - (page_speeds + np.random.normal(20, 1, 1000)) * 3

plt.scatter(page_speeds, purchase_amount)

slope, intercept, r_value, p_value, std_err = stats.linregress(page_speeds, purchase_amount)

r_value ** 2