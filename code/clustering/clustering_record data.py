#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Call required libraries
import numpy as np            # Data manipulation
import pandas as pd           # Dataframe manipulatio 
import matplotlib.pyplot as plt                   # For graphics
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
from sklearn.cluster import KMeans
from scipy.spatial.distance import squareform
from sklearn.preprocessing import StandardScaler  # For scaling dataset

wh1 = pd.read_csv("airqualityNew.csv") #Read the dataset
wh1.describe()

print("Dimension of dataset: wh1.shape")
wh1.dtypes

cor = wh1.corr() #Calculate the correlation of the above variables
sns.heatmap(cor, square = True) #Plot the correlation as heat map

### Clustering Of Countries
#Scaling of data
ss = StandardScaler()
ss.fit_transform(wh1)

##(1) k-means clustering
# find optimal k
def bestk(matrix, title): # plot out pairs of k and sse
    k_rng = range(1,6) #  if n = 5 then all vectors have itself as a center of different clusters
    sse = []
    for i in k_rng:
        km = KMeans(n_clusters = i)
        km.fit_predict(matrix)
        sse.append(km.inertia_ )

    plt.xlabel('K')
    plt.ylabel('sse')
    plt.title(str(title))
    plt.plot(k_rng,sse) 

bestk(wh1, 'K vs. SSE for record data')

#K means Clustering 
# k = 2
def doKmeans(X, nclust=2):
    model = KMeans(nclust)
    model.fit(X)
    clust_labels = model.predict(X)
    cent = model.cluster_centers_
    return (clust_labels, cent)

clust_labels, cent = doKmeans(wh1, 2)
kmeans = pd.DataFrame(clust_labels)
wh1.insert((wh1.shape[1]),'kmeans',kmeans)

#Plot the clusters obtained using k means
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(wh1['pm2.5'],wh1['pm10'],
                     c=kmeans[0],s=50)
ax.set_title('K-Means Clustering')
ax.set_xlabel('pm2.5')
ax.set_ylabel('pm10')
plt.colorbar(scatter)

# k = 3
def doKmeans(X, nclust=3):
    model = KMeans(nclust)
    model.fit(X)
    clust_labels = model.predict(X)
    cent = model.cluster_centers_
    return (clust_labels, cent)

clust_labels, cent = doKmeans(wh1, 3)
kmeans = pd.DataFrame(clust_labels)

#Plot the clusters obtained using k means
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(wh1['pm2.5'],wh1['pm10'],
                     c=kmeans[0],s=50)
ax.set_title('K-Means Clustering')
ax.set_xlabel('pm2.5')
ax.set_ylabel('pm10')
plt.colorbar(scatter)

# k = 4
def doKmeans(X, nclust=4):
    model = KMeans(nclust)
    model.fit(X)
    clust_labels = model.predict(X)
    cent = model.cluster_centers_
    return (clust_labels, cent)

clust_labels, cent = doKmeans(wh1, 4)
kmeans = pd.DataFrame(clust_labels)

#Plot the clusters obtained using k means
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(wh1['pm2.5'],wh1['pm10'],
                     c=kmeans[0],s=50)
ax.set_title('K-Means Clustering')
ax.set_xlabel('pm2.5')
ax.set_ylabel('pm10')
plt.colorbar(scatter)

######## hierarchical clustering with three distances
####### Use three different distance metrics
###### Visualize distances

## "euclidean"
from sklearn.metrics.pairwise import euclidean_distances
## Distance between each pair of rows (vectors)
Euc_dist=euclidean_distances(wh1)
print(Euc_dist)

sns.set(font_scale=3)
Z = linkage(squareform(np.around(euclidean_distances(wh1), 3)))

fig4 = plt.figure(figsize=(15, 15))
ax4 = fig4.add_subplot(111)
dendrogram(Z, ax=ax4)
ax4.tick_params(axis='x', which='major', labelsize=15)
ax4.tick_params(axis='y', which='major', labelsize=15)
#ax5 = fig4.add_subplot(212)
fig4.savefig('exampleSave.png')

## "manhattan"
from sklearn.metrics.pairwise import manhattan_distances
Man_dist=manhattan_distances(wh1)
print(Man_dist)

sns.set(font_scale=3)
Z = linkage(squareform(np.around(manhattan_distances(wh1), 3)))

fig4 = plt.figure(figsize=(15, 15))
ax4 = fig4.add_subplot(111)
dendrogram(Z, ax=ax4)
ax4.tick_params(axis='x', which='major', labelsize=15)
ax4.tick_params(axis='y', which='major', labelsize=15)
#ax5 = fig4.add_subplot(212)
fig4.savefig('exampleSave.png')

## "cosine_distances"
from sklearn.metrics.pairwise import cosine_distances
Cos_dist=cosine_distances(wh1)
print(Cos_dist)

sns.set(font_scale=5)
Z = linkage(squareform(np.around(cosine_distances(wh1), 5)))

fig4 = plt.figure(figsize=(15, 15))
ax4 = fig4.add_subplot(111)
dendrogram(Z, ax=ax4)
ax4.tick_params(axis='x', which='major', labelsize=15)
ax4.tick_params(axis='y', which='major', labelsize=15)
#ax5 = fig4.add_subplot(212)
fig4.savefig('exampleSave.png')

