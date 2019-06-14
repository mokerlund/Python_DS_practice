import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

page_speeds = np.random.normal(3, 1, 100)
purchase_amount = np.random.normal(50, 30, 100) / page_speeds

plt.scatter(page_speeds, purchase_amount)

#Splitting the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(page_speeds, purchase_amount, test_size=0.2)
plt.scatter(X_train, y_train)
plt.scatter(X_test, y_test)

x = np.array(X_train)
y = np.array(y_train)

#setting the refression line to 8th degree
p4 = np.poly1d(np.polyfit(x, y, 10))

#applying line
xp = np.linspace(0, 7, 100)
ax = plt.axes()
ax.set_xlim([0, 7])
ax.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')

X_test = np.array(X_test)
y_test = np.array(y_test)

ax.set_xlim([0, 7])
ax.set_ylim([50, -50])
plt.scatter(X_test, y_test)
plt.plot(xp, p4(xp), c='r')

r2 = r2_score(y_test, p4(X_test))
print(r2)

r2 = r2_score(np.array(y_train), p4(np.array(X_train)))
print(r2)