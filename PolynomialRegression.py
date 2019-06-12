import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)
page_speeds = np.random.normal(3, 1, 1000)
purchase_amount = np.random.normal(50, 10, 1000) / page_speeds

plt.scatter(page_speeds, purchase_amount)

#numpy has a polyfit function we can use
x = np.array(page_speeds)
y = np.array(purchase_amount)

p4 = np.poly1d(np.polyfit(x, y, 4))

#Visualize original plot with new regression line

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')

#Measuring the r-squared error
r2 = r2_score(y, p4(x))

print(r2)

#Activity- try different levels of polynomials

p4 = np.poly1d(np.polyfit(x, y, 2))
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')