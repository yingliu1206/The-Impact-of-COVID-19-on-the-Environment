#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:08:52 2020

@author: LiuYing
"""


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

##############################################################
STEMMER=PorterStemmer()
print(STEMMER.stem("fishings"))

# Use NLTK's PorterStemmer in a function
def MY_STEMMER(str_input):
    words = re.sub(r"[^A-Za-z\-]", " ", str_input).lower().split()
    words = [STEMMER.stem(word) for word in words]
    return words


import string
import numpy as np

##import spacy
## https://spacy.io/usage/spacy-101
# create a spaCy tokenizer


###########################
## Stemming and Lemming
## Stemming is different to Lemmatization 
## in the approach it uses to produce root 
## forms of words and the word produced.
##
##  !!! Stemming can result in words
##      That are not actually words. 
##    trouble, troubling, troubled, troubles ....
##    all become troubl

##Lemmatization is the process of grouping together 
##the different inflected forms of a word so they can
## be analysed as a single item. Lemmatization is similar
## to stemming but it brings context to the words. So it 
## links words with similar meaning to one word. 

#####################################################################

MyVect_STEM=CountVectorizer(input='filename',
                        analyzer = 'word',
                        stop_words='english',
                        ##stop_words=["and", "or", "but"],
                        #token_pattern='(?u)[a-zA-Z]+',
                        #token_pattern=pattern,
                        tokenizer=MY_STEMMER,
                        #strip_accents = 'unicode', 
                        lowercase = True
                        )


MyVect_STEM_Bern=CountVectorizer(input='filename',
                        analyzer = 'word',
                        stop_words='english',
                        ##stop_words=["and", "or", "but"],
                        #token_pattern='(?u)[a-zA-Z]+',
                        #token_pattern=pattern,
                        tokenizer=MY_STEMMER,
                        #strip_accents = 'unicode', 
                        lowercase = True,
                        binary=True
                        )



MyVect_IFIDF=TfidfVectorizer(input='filename',
                        analyzer = 'word',
                        stop_words='english',
                        lowercase = True,
                        #binary=True
                        )

MyVect_IFIDF_STEM=TfidfVectorizer(input='filename',
                        analyzer = 'word',
                        stop_words='english',
                        tokenizer=MY_STEMMER,
                        #strip_accents = 'unicode', 
                        lowercase = True,
                        #binary=True
                        )
#

#We will be creating new data frames - one for NB and one for Bern. 
## These are the two new and currently empty DFs
FinalDF_STEM=pd.DataFrame()
FinalDF_STEM_Bern=pd.DataFrame()
FinalDF_TFIDF=pd.DataFrame()
FinalDF_TFIDF_STEM=pd.DataFrame()


## You will need to know where things are on your computer.
## This code assumes that it is in the same folder/location
## as the folders DOG and HIKE. It will loop through the files in
## these two folders and will build the list needed to use
## CounterVectorizer. 
## NOTICE: My loop has a path in it. This is for MY computer - not yours!
## You will need to adjust the path.

for name in ["DOG", "HIKE"]:

    builder=name+"DF"
    #print(builder)
    builderB=name+"DFB"
    path="/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/code/Decision Tree/"+name
    
    FileList=[]
    for item in os.listdir(path):
        #print(path+ "/" + item)
        next=path+ "/" + item
        FileList.append(next)  
        print("full list...")
        #print(FileList)
        
        ## Do for all three
        ## MyVect_STEM  and MyVect_IFIDF and MyVect_IFIDF_STEM
        X1=MyVect_STEM.fit_transform(FileList)
        X2=MyVect_IFIDF.fit_transform(FileList)
        X3=MyVect_IFIDF_STEM.fit_transform(FileList)
        XB=MyVect_STEM_Bern.fit_transform(FileList)
        
        
        ColumnNames1=MyVect_STEM.get_feature_names()
        NumFeatures1=len(ColumnNames1)
        ColumnNames2=MyVect_IFIDF.get_feature_names()
        NumFeatures2=len(ColumnNames2)
        ColumnNames3=MyVect_IFIDF_STEM.get_feature_names()
        NumFeatures3=len(ColumnNames3)
        ColumnNamesB=MyVect_STEM_Bern.get_feature_names()
        NumFeatures4=len(ColumnNamesB)
        #print("Column names: ", ColumnNames2)
        #Create a name
        
   
    builderS=pd.DataFrame(X1.toarray(),columns=ColumnNames1)
    builderT=pd.DataFrame(X2.toarray(),columns=ColumnNames2)
    builderTS=pd.DataFrame(X3.toarray(),columns=ColumnNames3)
    builderB=pd.DataFrame(XB.toarray(),columns=ColumnNamesB)
    
    ## Add column
    #print("Adding new column....")
    builderS["Label"]=name
    builderT["Label"]=name
    builderTS["Label"]=name
    builderB["Label"]=name
    #print(builderS)
    
    FinalDF_STEM= FinalDF_STEM.append(builderS)
    FinalDF_STEM_Bern= FinalDF_STEM_Bern.append(builderB)
    FinalDF_TFIDF= FinalDF_TFIDF.append(builderT)
    FinalDF_TFIDF_STEM= FinalDF_TFIDF_STEM.append(builderTS)
   
    #print(FinalDF_STEM.head())


## Replace the NaN with 0 because it actually 
## means none in this case
FinalDF_STEM=FinalDF_STEM.fillna(0)
FinalDF_STEM_Bern=FinalDF_STEM_Bern.fillna(0)
FinalDF_TFIDF=FinalDF_TFIDF.fillna(0)
FinalDF_TFIDF_STEM=FinalDF_TFIDF_STEM.fillna(0)

###### REMOVE number columns
## Remove columns with number from this one
##-------------------------------------------------------------------
####### Create a function that removes columns that are/contain nums
##-------------------------------------------------------------------

def RemoveNums(SomeDF):
    #print(SomeDF)
    print("Running Remove Numbers function....\n")
    temp=SomeDF
    MyList=[]
    for col in temp.columns:
        #print(col)
        #Logical1=col.isdigit()  ## is a num
        Logical2=str.isalpha(col) ## this checks for anything
        ## that is not a letter
        if(Logical2==False):# or Logical2==True):
            #print(col)
            MyList.append(str(col))
            #print(MyList)       
    temp.drop(MyList, axis=1, inplace=True)
            #print(temp)
            #return temp
       
    return temp
##########################################################

## Call the function ....
FinalDF_STEM=RemoveNums(FinalDF_STEM)
FinalDF_STEM_Bern=RemoveNums(FinalDF_STEM_Bern)
FinalDF_TFIDF=RemoveNums(FinalDF_TFIDF)
FinalDF_TFIDF_STEM=RemoveNums(FinalDF_TFIDF_STEM)

## Have a look:
## These print statements help you to see where you are
#print(FinalDF_STEM)
## Remove columns that contain "-"  HOW TO....
#cols = [c for c in FinalDF_STEM.columns if "-" in c[:] ]
#FinalDF_STEM=FinalDF_STEM.drop(cols, axis = 1) 
print(FinalDF_STEM)
print(FinalDF_STEM_Bern)
print(FinalDF_TFIDF)
print(FinalDF_TFIDF_STEM)

##################################################
##
##        Now we have 4 labeled dataframes!
##
##        Let's model them.....
##
######################################################

## Create the testing set - grab a sample from the training set. 
## Be careful. Notice that right now, our train set is sorted by label.
## If your train set is large enough, you can take a random sample.
from sklearn.model_selection import train_test_split
import random as rd
rd.seed(1234)
TrainDF1, TestDF1 = train_test_split(FinalDF_STEM, test_size=0.3)
TrainDF2, TestDF2 = train_test_split(FinalDF_TFIDF, test_size=0.3)
TrainDF3, TestDF3 = train_test_split(FinalDF_TFIDF_STEM, test_size=0.3)
TrainDF4, TestDF4 = train_test_split(FinalDF_STEM_Bern, test_size=0.4)

### OK - at this point we have Train and Test data for the text data
## in DOG and HIKE. 
## Of course, this can be updated to work from sentiment (like POS and NEG)
## and can be update for multiple folders or one folder..




###############################################
## For all three DFs - separate LABELS
#################################################
## IMPORTANT - YOU CANNOT LEAVE LABELS ON THE TEST SET
## Save labels
### TEST ---------------------
Test1Labels=TestDF1["Label"]
Test2Labels=TestDF2["Label"]
Test3Labels=TestDF3["Label"]
Test4Labels=TestDF4["Label"]
print(Test2Labels)
## remove labels
TestDF1 = TestDF1.drop(["Label"], axis=1)
TestDF2 = TestDF2.drop(["Label"], axis=1)
TestDF3 = TestDF3.drop(["Label"], axis=1)
TestDF4 = TestDF4.drop(["Label"], axis=1)
print(TestDF1)

## TRAIN ----------------------------
Train1Labels=TrainDF1["Label"]
Train2Labels=TrainDF2["Label"]
Train3Labels=TrainDF3["Label"]
Train4Labels=TrainDF4["Label"]
print(Train3Labels)
## remove labels
TrainDF1 = TrainDF1.drop(["Label"], axis=1)
TrainDF2 = TrainDF2.drop(["Label"], axis=1)
TrainDF3 = TrainDF3.drop(["Label"], axis=1)
TrainDF4 = TrainDF4.drop(["Label"], axis=1)
print(TrainDF3)


####################################################################
########################### Naive Bayes ############################
####################################################################
from sklearn.naive_bayes import MultinomialNB
#https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB.fit
#Create the modeler
MyModelNB= MultinomialNB()



## Run on all three Dfs.................
NB1=MyModelNB.fit(TrainDF1, Train1Labels)
Prediction1 = MyModelNB.predict(TestDF1)
print(np.round(MyModelNB.predict_proba(TestDF1),2))

NB2=MyModelNB.fit(TrainDF2, Train2Labels)
Prediction2 = MyModelNB.predict(TestDF2)
print(np.round(MyModelNB.predict_proba(TestDF2),2))

NB3=MyModelNB.fit(TrainDF3, Train3Labels)
Prediction3 = MyModelNB.predict(TestDF3)
print(np.round(MyModelNB.predict_proba(TestDF3),2))

NB4=MyModelNB.fit(TrainDF4, Train4Labels)
Prediction4 = MyModelNB.predict(TestDF4)
print(np.round(MyModelNB.predict_proba(TestDF4),2))



print("\nThe prediction from NB is:")
print(Prediction1)
print("\nThe actual labels are:")
print(Test1Labels)

print("\nThe prediction from NB is:")
print(Prediction2)
print("\nThe actual labels are:")
print(Test2Labels)

print("\nThe prediction from NB is:")
print(Prediction3)
print("\nThe actual labels are:")
print(Test3Labels)

print("\nThe prediction from NB is:")
print(Prediction4)
print("\nThe actual labels are:")
print(Test4Labels)

## confusion matrix
from sklearn.metrics import confusion_matrix
## The confusion matrix is square and is labels X labels
## We ahve two labels, so ours will be 2X2
#The matrix shows
## rows are the true labels
## columns are predicted
## it is al[habetical
## The numbers are how many 
cnf_matrix1 = confusion_matrix(Test1Labels, Prediction1)
print("\nThe confusion matrix is:")
print(cnf_matrix1)

cnf_matrix2 = confusion_matrix(Test2Labels, Prediction2)
print("\nThe confusion matrix is:")
print(cnf_matrix2)

cnf_matrix3 = confusion_matrix(Test3Labels, Prediction3)
print("\nThe confusion matrix is:")
print(cnf_matrix3)

cnf_matrix4 = confusion_matrix(Test4Labels, Prediction4)
print("\nThe confusion matrix is:")
print(cnf_matrix4)


#######################################################
### Bernoulli #########################################
#######################################################


from sklearn.naive_bayes import BernoulliNB
BernModel = BernoulliNB()
BernModel.fit(TrainDF4, Train4Labels)
##BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
print("\nBernoulli prediction:\n")
Prediction=BernModel.predict(TestDF4)
print("\nActual:")
print(Test4Labels)
print("\The prediction\n")
print(Prediction)
#
bn_matrix = confusion_matrix(Test4Labels, Prediction)
print("\nThe confusion matrix is:")
print(bn_matrix)


#########################################################
#############    Decision Trees   #######################
#########################################################

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
## conda install python-graphviz
## restart kernel (click the little red x next to the Console)
import graphviz 
from sklearn.metrics import confusion_matrix

#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
MyDT=DecisionTreeClassifier(criterion='entropy', ##"entropy" or "gini"
                            splitter='best',  ## or "random" or "best"
                            max_depth=None, 
                            min_samples_split=2, 
                            min_samples_leaf=1, 
                            min_weight_fraction_leaf=0.0, 
                            max_features=None, 
                            random_state=None, 
                            max_leaf_nodes=None, 
                            min_impurity_decrease=0.0, 
                            min_impurity_split=None, 
                            class_weight=None)


## ------------------------------
## This for loop will fit and predict Decision Trees for 
## all 4 of the dataframes. Notice that this uses dynamic variables
## and eval
##--------------------------
##
#print(TrainDF1.columns)


for i in [1,2,3,4]:
    temp1=str("TrainDF"+str(i))
    temp2=str("Train"+str(i)+"Labels")
    temp3=str("TestDF"+str(i))
    temp4=str("Test"+str(i)+"Labels")
    
    ## perform DT
    MyDT.fit(eval(temp1), eval(temp2))
    ## plot the tree
    tree.plot_tree(MyDT)
    plt.savefig(temp1)
    feature_names=eval(str(temp1+".columns"))
    dot_data = tree.export_graphviz(MyDT, out_file=None,
                    ## The following creates TrainDF.columns for each
                    ## which are the feature names.
                      feature_names=eval(str(temp1+".columns")),  
                      #class_names=MyDT.class_names,  
                      filled=True, rounded=True,  
                      special_characters=True)                                    
    graph = graphviz.Source(dot_data) 
    ## Create dynamic graph name
    tempname=str("Graph" + str(i))
    graph.render(tempname) 
    ## Show the predictions from the DT on the test set
    print("\nActual for DataFrame: ", i, "\n")
    print(eval(temp2))
    print("Prediction\n")
    DT_pred=MyDT.predict(eval(temp3))
    print(DT_pred)
    ## Show the confusion matrix
    bn_matrix = confusion_matrix(eval(temp4), DT_pred)
    print("\nThe confusion matrix is:")
    print(bn_matrix)
    FeatureImp=MyDT.feature_importances_   
    indices = np.argsort(FeatureImp)[::-1]
    ## print out the important features.....
    for f in range(TrainDF4.shape[1]):
        if FeatureImp[indices[f]] > 0:
            print("%d. feature %d (%f)" % (f + 1, indices[f], FeatureImp[indices[f]]))
            print ("feature name: ", feature_names[indices[f]])

## FYI for small datasets you can zip features....
## print(dict(zip(iris_pd.columns, clf.feature_importances_)))






#####################################################
##  Visualize Decision Trees plotting paired surfaces
##
####################################################
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

f1=TrainDF1.columns.get_loc("dog") 
f2=TrainDF1.columns.get_loc("hike") 
f3=TrainDF1.columns.get_loc("workout") 
f4=TrainDF1.columns.get_loc("pollution") 


n_classes =2
plot_colors = "ryb"
plot_step = 0.02

for pairidx, pair in enumerate([[f1, f2], [f1, f3], [f1, f4],
                                [f2,f3], [f3, f4]]):
    #print(TrainDF1.iloc[:,pair])
    X = TrainDF1.iloc[:, pair]
    ## Because we are plotting, using our GOD and HIKE labels will not work
    ## we need to change them to 0 and 1
    y = Train1Labels
    print(y)
    oldy=y
    #print(type(y))
    y=y.replace("DOG", 1)
    y=y.replace("HIKE", 0)
    
    print(y)
    # Train
    DT = DecisionTreeClassifier().fit(X, y)
    # Plot the decision boundary
    plt.subplot(2, 3, pairidx + 1)

    x_min, x_max = X.iloc[:, 0].min() - 1, X.iloc[:, 0].max() + 1
    print(x_min)
    y_min, y_max = X.iloc[:, 1].min() - 1, X.iloc[:, 1].max() + 1
   
    xx, yy = np.meshgrid(np.arange(x_min, x_max,plot_step),
                         np.arange(y_min, y_max,plot_step))
    
    #print(yy)
    
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)
#
    Z = DT.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    print(Z)
    
    
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)
       
    plt.scatter(X.iloc[:, 0], X.iloc[:, 1], s=30, label=oldy,edgecolor='black', 
                    #c=color, s=15)
                    #label=y[i],
                    cmap=plt.cm.RdYlBu)
###---------------------------end for loop ----------------------------------
#plt.suptitle("Decision surface of a decision tree using paired features")
#plt.legend(loc='lower right', borderpad=0, handletextpad=0)
#plt.axis("tight")
#
#plt.figure()

#########################################################
##
##                 Random Forest for Text Data
##
#################################################################
RF = RandomForestClassifier()
RF.fit(TrainDF1, Train1Labels)
RF_pred=RF.predict(TestDF1)

bn_matrix_RF_text = confusion_matrix(Test1Labels, RF_pred)
print("\nThe confusion matrix is:")
print(bn_matrix_RF_text)

################# VIS RF---------------------------------
## FEATURE NAMES...................
FeaturesT=TrainDF1.columns
#Targets=StudentTestLabels_Num

figT, axesT = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)

tree.plot_tree(RF.estimators_[0],
               feature_names = FeaturesT, 
               #class_names=Targets,
               filled = True)

##save it
figT.savefig('RF_Tree_Text')  ## creates png

#####------------------> View estimator Trees in RF

figT2, axesT2 = plt.subplots(nrows = 1,ncols = 5,figsize = (10,2), dpi=900)

for index in range(0, 5):
    tree.plot_tree(RF.estimators_[index],
                   feature_names = FeaturesT, 
                   filled = True,
                   ax = axesT2[index])

    axesT2[index].set_title('Estimator: ' + str(index), fontsize = 11)
## Save it
figT2.savefig('FIVEtrees_RF.png')

#################-------------------------->
## Feature importance in RF
##-----------------------------------------
## Recall that FeaturesT are the columns names - the words in this case.
######
FeatureImpRF=RF.feature_importances_   
indicesRF = np.argsort(FeatureImpRF)[::-1]
## print out the important features.....
for f2 in range(TrainDF1.shape[1]):   ##TrainDF1.shape[1] is number of columns
    if FeatureImpRF[indicesRF[f2]] >= 0.01:
        print("%d. feature %d (%.2f)" % (f2 + 1, indicesRF[f2], FeatureImpRF[indicesRF[f2]]))
        print ("feature name: ", FeaturesT[indicesRF[f2]])
        

## PLOT THE TOP 10 FEATURES...........................
top_ten_arg = indicesRF[:10]
#print(top_ten_arg)
plt.title('Feature Importances Environment and Policy')
plt.barh(range(len(top_ten_arg)), FeatureImpRF[top_ten_arg], color='b', align='center')
plt.yticks(range(len(top_ten_arg)), [FeaturesT[i] for i in top_ten_arg])
plt.xlabel('Relative Importance')
plt.show()