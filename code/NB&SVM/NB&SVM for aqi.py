#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Textmining Naive Bayes Example
import nltk
from sklearn import preprocessing
import pandas as pd
import sklearn
import re  
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
## For Stemming
from nltk.tokenize import sent_tokenize, word_tokenize
import os
from sklearn.model_selection import train_test_split
import random as rd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
## conda install python-graphviz
## restart kernel (click the little red x next to the Console)
import graphviz 
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.svm import LinearSVC
from sklearn.decomposition import PCA
#from mpl_toolkits.mplot3d import Axes3D 
## conda install python-graphviz
## restart kernel (click the little red x next to the Console)
import graphviz 
from sklearn.metrics import confusion_matrix

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
## conda install pydotplus
import pydotplus
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

#from nltk.stem import WordNetLemmatizer 
#LEMMER = WordNetLemmatizer() 

from nltk.stem.porter import PorterStemmer


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

##################################################################
#############   PART 2 Using the Student Dataset #################
##################################################################

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## The student dataset is not text data and so does not need to be 
## vectorized.
## Also, the student dataset is clean. This will not normally
## be the case.

#####################################################################

## Read the data into a dataframe
## DATA: Just numeric and record labeled data
## https://drive.google.com/file/d/1uXtDBIP-dTbFNXbZC0DcCKxIXjocW3xF/view?usp=sharing
## ## There is also another dataset for which the labels are numbers and not words...
## https://drive.google.com/file/d/1g0go050nV02Fibk_9RGpBRGnMwIGQZu5/view?usp=sharing

########################################################################################
filenameNum="/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/covid19_by_aqi.csv"
#filenameNum="C:/Users/profa/Documents/Python Scripts/ANLY503/DATA/StudentSummerProgramData_Numeric_NumLabeled.csv"
StudentDF_Num=pd.read_csv(filenameNum)
StudentDF_Num=StudentDF_Num.drop(['Countries', 'WHO Region'], axis=1)
print(StudentDF_Num.head())
################# Sklearn methods such as these do not run on mixed type data...
#filenameMixed="C:/Users/profa/Documents/Python Scripts/ANLY503/DATA/StudentSummerProgramData_Mixed_Labeled.csv"
#StudentDF_Mix=pd.read_csv(filenameMixed)
#print(StudentDF_Mix.head())

### Because the data is already clean and ready - I can seperate it
## into TRAINING and TESTING sets
####-----------------------------------------------
#from sklearn.model_selection import train_test_split
StudentTrainDF_Num, StudentTestDF_Num = train_test_split(StudentDF_Num, test_size=0.3)
#StudentTrainDF_Mix, StudentTestDF_Mix = train_test_split(StudentDF_Mix, test_size=0.3)

######## Seperate LABELS FROM DATA--------------------
## Make sure you know the name of the label
## For both datasets above  - in this case - it is "Decision"
## TEST - Num
StudentTestLabels_Num=StudentTestDF_Num["Label"]  ## save labels
print(StudentTestLabels_Num)
StudentTestData_Num = StudentTestDF_Num.drop(["Label"], axis=1)  ##drop labels
print(StudentTestData_Num)

## TRAIN - Num
StudentTrainLabels_Num=StudentTrainDF_Num["Label"]  ## save labels
print(StudentTrainLabels_Num)
StudentTrainData_Num = StudentTrainDF_Num.drop(["Label"], axis=1)  ##drop labels
print(StudentTrainData_Num)

### TEST - Mixed
#StudentTestLabels_Mix=StudentTestDF_Mix["Decision"]  ## save labels
#print(StudentTestLabels_Mix)
#StudentTestData_Mix = StudentTestDF_Mix.drop(["Decision"], axis=1)  ##drop labels
#print(StudentTestData_Mix)
#
### TRAIN - Mixed
#StudentTrainLabels_Mix=StudentTrainDF_Mix["Decision"]  ## save labels
#print(StudentTrainLabels_Mix)
#StudentTrainData_Mix = StudentTrainDF_Mix.drop(["Decision"], axis=1)  ##drop labels
#print(StudentTrainData_Mix)

#print(StudentTestLabels_Num)
#print(StudentTestData_Num)
### TRAIN - Num
#print(StudentTrainLabels_Num)
#print(StudentTrainData_Num)
###############################################
## SCALE ALL DATA to between 0 and 1
#from sklearn import preprocessing
###########################################################
x = StudentTrainData_Num.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
StudentTrainData_Num_S = pd.DataFrame(x_scaled)

x2 = StudentTestData_Num.values #returns a numpy array
min_max_scaler2 = preprocessing.MinMaxScaler()
x_scaled2 = min_max_scaler2.fit_transform(x2)
StudentTestData_Num_S = pd.DataFrame(x_scaled2)
print(StudentTestData_Num_S)


####################################################################
########################### Naive Bayes ############################
####################################################################
#from sklearn.naive_bayes import MultinomialNB
#https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB.fit
#Create the modeler

############# In Python - unlike R - you cannot run a standard NB on 
## Mixed data. Therefore, we will only run it on our numeric dataset.
##################
MyModelNB_Num= MultinomialNB()

## When you look up this model, you learn that it wants the 
## DF seperate from the labels

MyModelNB_Num.fit(StudentTrainData_Num, StudentTrainLabels_Num)
PredictionNB = MyModelNB_Num.predict(StudentTestData_Num)
#print("\nThe prediction from NB is:")
#print(PredictionNB)
#print("\nThe actual labels are:")
#print(StudentTestLabels_Num)
## confusion matrix
#from sklearn.metrics import confusion_matrix
## The confusion matrix is square and is labels X labels
## We ahve two labels, so ours will be 2X2
#The matrix shows
## rows are the true labels
## columns are predicted
## it is al[habetical
## The numbers are how many 
cnf_matrix = confusion_matrix(StudentTestLabels_Num, PredictionNB)
print("\nThe confusion matrix is:")
print(cnf_matrix)
### prediction probabilities
## columns are the labels in alphabetical order
## The decinal in the matrix are the prob of being
## that label
print(np.round(MyModelNB_Num.predict_proba(StudentTestData_Num),2))
MyModelNB_Num.get_params(deep=True)

from sklearn.decomposition import PCA
#from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
## remap labels to numbers to view
ymap=StudentTrainLabels_Num
ymap=ymap.replace("AQI below average", 1)
ymap=ymap.replace("AQI at or above average", 0)

pca = PCA(n_components=2)
proj = pca.fit_transform(StudentTrainData_Num)
plt.scatter(proj[:, 0], proj[:, 1], c=ymap, cmap="Paired")
plt.colorbar()

## VIS
import seaborn as sns
sns.heatmap(cnf_matrix.T, square=True, annot=True, fmt='d', 
            xticklabels=["AQI at or above average", "AQI below average"], yticklabels=["AQI at or above average", "AQI below average"])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')



##@@@@@@@@@@@@@@@@@@@@@@@
#############################################
###########  SVM ############################
#############################################
#from sklearn.svm import LinearSVC
### NOTE - We CANNOT use SVM directly on the data. 
### SVMs do not run on qualitative data.
    
############  MUST NORMALIZE THE DATA!!  ################
    ## This is done above. Notice the _S for scale after each DF


##-----


SVM_Model1=LinearSVC(C=1)
SVM_Model1.fit(StudentTrainData_Num_S, StudentTrainLabels_Num)

#print("SVM prediction:\n", SVM_Model1.predict(StudentTestData_Num_S))
#print("Actual:")
#print(StudentTestLabels_Num)

SVM_matrix = confusion_matrix(StudentTestLabels_Num, SVM_Model1.predict(StudentTestData_Num_S))
print("\nThe confusion matrix is:")
print(SVM_matrix)
print("\n\n")

## VIS
import seaborn as sns
sns.heatmap(SVM_matrix.T, square=True, annot=True, fmt='d', 
            xticklabels=["AQI at or above average", "AQI below average"], yticklabels=["AQI at or above average", "AQI below average"])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')

#--------------other kernels
## RBF
SVM_Model2=sklearn.svm.SVC(C=1, kernel='rbf', degree=3, gamma="auto")
SVM_Model2.fit(StudentTrainData_Num_S, StudentTrainLabels_Num)

#print("SVM prediction:\n", SVM_Model2.predict(StudentTestData_Num_S))
#print("Actual:")
#print(StudentTestLabels_Num)

SVM_matrix2 = confusion_matrix(StudentTestLabels_Num, SVM_Model2.predict(StudentTestData_Num_S))
print("\nThe confusion matrix is:")
print(SVM_matrix2)
print("\n\n")

## VIS
import seaborn as sns
sns.heatmap(SVM_matrix2.T, square=True, annot=True, fmt='d', 
            xticklabels=["AQI at or above average", "AQI below average"], yticklabels=["AQI at or above average", "AQI below average"])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')
##------------------------------
## POLY
SVM_Model3=sklearn.svm.SVC(C=100, kernel='poly', degree=3, gamma="auto")
SVM_Model3.fit(StudentTrainData_Num_S, StudentTrainLabels_Num)

#print("SVM prediction:\n", SVM_Model3.predict(StudentTestData_Num_S))
#print("Actual:")
#print(StudentTestLabels_Num)

SVM_matrix3 = confusion_matrix(StudentTestLabels_Num, SVM_Model3.predict(StudentTestData_Num_S))
print("\nThe confusion matrix is:")
print(SVM_matrix3)
print("\n\n")

## VIS
import seaborn as sns
sns.heatmap(SVM_matrix3.T, square=True, annot=True, fmt='d', 
            xticklabels=["AQI at or above average", "AQI below average"], yticklabels=["AQI at or above average", "AQI below average"])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')



