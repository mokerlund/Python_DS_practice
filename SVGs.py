import numpy as np
import matplotlib.pyplot
from pylab import *
from sklearn.preprocessing import MinMaxScaler
from sklearn import svm, datasets

#Create fake income/age clusters for N people in k clusters
def create_clustered_data(N, k):
    np.random.seed(1234)
    points_per_cluster = float(N)/k
    X =[]
    y = []
    for i in range (k):
        income_centroid = np.random.uniform(20000, 200000)
        age_centroid = np.random.uniform(20, 70)
        for j in range(int(points_per_cluster)):
            X.append([np.random.normal(income_centroid, 10000), np.random.normal(age_centroid, 2)])
            y.append(i)
    X = np.array(X)
    y = np.array(y)
    return X, y

(X, y) = create_clustered_data(100, 5)

plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))

scaling = MinMaxScaler(feature_range=(-1,1)).fit(X)
X = scaling.transform(X)

plt.figure(figsize=(8,6))
plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))

C = 1.0
svc = svm.SVC(kernel='linear', C=C).fit(X,y)

def plot_predictions(clf):
    #Create a dense grid of points to sample
    xx, yy = np.meshgrid(np.arange(-1, 1, .001), np.arange(-1, 1, .001))
    
    #convert to numpy arrays
    npx = xx.ravel()
    npy = yy.ravel()

    sample_points = np.c_[npx, npy]

    #Generate predicted labels(cluster numbers) for each point
    Z = clf.predict(sample_points)

    plt.figure(figsize=(8,6))
    Z = Z.reshape(xx.shape) #Reshape results to match xx dimension
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8) #Draw the contour
    plt.scatter(X[:,0], X[:,1], c=y.astype(np.float)) #Draw the points

plot_predictions(svc)