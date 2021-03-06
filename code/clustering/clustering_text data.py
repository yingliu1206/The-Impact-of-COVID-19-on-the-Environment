#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sklearn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import squareform
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.manifold import MDS
from mpl_toolkits.mplot3d import Axes3D

import seaborn as sns

# get the text data
List_Of_Files = ['environment1.rtf', 'environment2.rtf',
                 'environment3.rtf', 'environment4.rtf',
                 'environment5.rtf', 'environment6.rtf'
                 ]

# use the CountVectorizer
vectorizer = CountVectorizer(input='filename', stop_words="english")  # Using input='filename' means that fit_transform will

# create a sparse matrix
dtm = vectorizer.fit_transform(List_Of_Files)  

# words list
words = vectorizer.get_feature_names()

# convert to a regular array
dtm = dtm.toarray()

# Change to Dataframe
files = pd.DataFrame(dtm, columns=words)

# clean the text data
for nextcol in files.columns:
    if (re.search(r'[^A-Za-z]+', nextcol)):  ## find non chars
        files = files.drop([nextcol], axis=1)

        ## remove columns with words <= 4
    elif (len(str(nextcol)) <= 4):
        files = files.drop([nextcol], axis=1)

# check it
print(files)

#create a wordcloud for common words  
comment_words = '' 
stopwords = set(STOPWORDS) 
  
# iterate through files 
for val in files: 
      
    # typecaste each val to string 
    val = str(val) 
  
    # split the value 
    tokens = val.split() 
      
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
      
    comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 

# plot the WordCloud image                          
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 


######## Clustering with kmeans
#### find optimal k
def bestk(matrix, title): # plot out pairs of k and sse
    k_rng = range(1,7) #  if n = 6 then all vectors have itself as a center of different clusters
    sse = []
    for i in k_rng:
        km = KMeans(n_clusters = i)
        km.fit_predict(matrix)
        sse.append(km.inertia_ )

    plt.xlabel('K')
    plt.ylabel('sse')
    plt.title(str(title))
    plt.plot(k_rng,sse) 

bestk(files, 'K vs. SSE for text data')
## It shows that  k=2  is the optimal choice of k. Now we can plot the Kmeans clustering with k=3 .

#### kmeans visualized by 2d
def PCA_data(n, data): # we can plot it with two unit vectors that have the most variance (pincipal component)
    pc_data = PCA(n_components=n)
    pc_data.fit(data)
    data2 = pc_data.transform(data)
    return (data2)

PCA_corpus = PCA_data(2,files)
plt.scatter(PCA_corpus[:,0], PCA_corpus[:,1], color = 'blue')
plt.xlabel('principal component 1')
plt.ylabel('principal component 2')
plt.title('simple 2d scatter plot of text data with PCA')
plt.show()  
## This is how the two clusters look like with PCA. 

##### kmeans visualized by 3d    
kmeans_object_Count = sklearn.cluster.KMeans(n_clusters=2)
#print(kmeans_object)
kmeans_object_Count.fit(files)
# Get cluster assignment labels
labels = kmeans_object_Count.labels_
prediction_kmeans = kmeans_object_Count.predict(files)
#print(labels)
print(prediction_kmeans)
# Format results as a DataFrame
Myresults = pd.DataFrame([files.index,labels]).T
print(Myresults)
Myresults[Myresults.index == 1]

############# ---> ALWAYS USE VIS! ----------
print(files)
x=files["abandon"]  ## col 1  starting from 0
y=files["ability"]  ## col 3  starting from 1
z=files["yield"]  ## col 2208  starting from 1
colnames=files.columns
print(colnames)
#print(x,y,z)
fig1 = plt.figure(figsize=(12, 12))
ax1 = Axes3D(fig1, rect=[0, 0, .90, 1], elev=48, azim=134)

ax1.scatter(x,y,z, cmap="RdYlGn", edgecolor='k', s=200,c=prediction_kmeans)
ax1.w_xaxis.set_ticklabels([])
ax1.w_yaxis.set_ticklabels([])
ax1.w_zaxis.set_ticklabels([])

ax1.set_xlabel('abandon', fontsize=25)
ax1.set_ylabel('ability', fontsize=25)
ax1.set_zlabel('yield', fontsize=25)
plt.show()
        
######## hierarchical clustering with three distances
####### Use three different distance metrics
###### Visualize distances

## "euclidean"
from sklearn.metrics.pairwise import euclidean_distances
## Distance between each pair of rows (vectors)
Euc_dist=euclidean_distances(files)
print(Euc_dist)

sns.set(font_scale=3)
Z = linkage(squareform(np.around(euclidean_distances(files), 3)))

fig4 = plt.figure(figsize=(15, 15))
ax4 = fig4.add_subplot(111)
dendrogram(Z, ax=ax4)
ax4.tick_params(axis='x', which='major', labelsize=15)
ax4.tick_params(axis='y', which='major', labelsize=15)
#ax5 = fig4.add_subplot(212)
fig4.savefig('exampleSave.png')

## "manhattan"
from sklearn.metrics.pairwise import manhattan_distances
Man_dist=manhattan_distances(files)
print(Man_dist)

sns.set(font_scale=3)
Z = linkage(squareform(np.around(manhattan_distances(files), 3)))

fig4 = plt.figure(figsize=(15, 15))
ax4 = fig4.add_subplot(111)
dendrogram(Z, ax=ax4)
ax4.tick_params(axis='x', which='major', labelsize=15)
ax4.tick_params(axis='y', which='major', labelsize=15)
#ax5 = fig4.add_subplot(212)
fig4.savefig('exampleSave.png')

## "cosine_distances"
from sklearn.metrics.pairwise import cosine_distances
Cos_dist=cosine_distances(files)
print(Cos_dist)

sns.set(font_scale=3)
Z = linkage(squareform(np.around(cosine_distances(files), 3)))

fig4 = plt.figure(figsize=(15, 15))
ax4 = fig4.add_subplot(111)
dendrogram(Z, ax=ax4)
ax4.tick_params(axis='x', which='major', labelsize=15)
ax4.tick_params(axis='y', which='major', labelsize=15)
#ax5 = fig4.add_subplot(212)
fig4.savefig('exampleSave.png')

