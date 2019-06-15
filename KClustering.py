#Create fake income data that includes people clustered by income and age, randomly
#For N people in K clusters
import numpy as np
import matplotlib.pyplot as plt
from  sklearn.cluster import KMeans
from sklearn.preprocessing import scale

def create_clustered_data(N, k):
    np.random.seed(10)
    points_per_cluster = float(N)/k
    X = []
    for i in range(k):
        income_centroid = np.random.uniform(20000.0, 200000.0)
        age_centroid = np.random.uniform(20.0, 70.0)
        for j in range(int(points_per_cluster)):
            X.append([np.random.normal(income_centroid, 10000.0), np.random.normal(age_centroid, 2.0)])
        X = np.array(X)
        return X

#Use K-means to rediscover these clusters in unsupervised learning:
df = create_clustered_data(100, 5)

model = KMeans(n_clusters=5)
#scaling data to normalize it
model = model.fit(scale(df))
#we can look at the clusters each data point was assigned to
print(model.labels_)

#visualizing it
plt.figure(figsize=(8, 6))
plt.scatter(df[:,0], df[:,1], c=model.labels_.astype(np.float))