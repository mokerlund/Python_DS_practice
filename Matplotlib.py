import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

##Matplotlib Tricks & Tips
x = np.arange(-3, 3, 0.001)

#Save Graph as a file
#plt.savfig('C://path/filename.png', format='png' )

#Adjusting the axis + adding Gridlines

axes = plt.axes()
axes.set_xlim(-5, 5)
axes.set_ylim(0, 1.0)
axes.set_xticks([-5. -4. -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
axes.grid()
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1, .5))
plt.show()

#Change types and colors
plt.plot(x, norm.pdf(x), 'b-')
plt.plot(x, norm.pdf(x, 1, .5), 'r:')

#Labeling axis and adding legend

plt.xlabel('Greebles')
plt.ylabel('Probability')
plt.legend(['Sneeches', 'Gacks'], loc=4)


#XKCD style (ironic-memey style)

plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([-30, 10])

df = np.ones(100)
df[70:] -= np.arange(30)

plt.annotate('My happiness in the morning when I remember I have work', xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

plt.plot(df)

plt.xlabel('time')
plt.ylabel('my happiness')

plt.savefig('~/memegraph.png', format='png')