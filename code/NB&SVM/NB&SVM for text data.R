library(tm)
#install.packages("tm")
library(stringr)
library(wordcloud)
# ONCE: install.packages("Snowball")
## NOTE Snowball is not yet available for R v 3.5.x
## So I cannot use it  - yet...
##library("Snowball")
##set working directory
## ONCE: install.packages("slam")
library(slam)
library(quanteda)
## ONCE: install.packages("quanteda")
## Note - this includes SnowballC
library(SnowballC)
library(arules)
##ONCE: install.packages('proxy')
library(proxy)
library(cluster)
library(stringi)
library(proxy)
library(Matrix)
library(tidytext) # convert DTM to DF
library(plyr) ## for adply
library(ggplot2)
library(factoextra) # for fviz
library(mclust) # for Mclust EM clustering

library(naivebayes)
#Loading required packages
#install.packages('tidyverse')
library(tidyverse)
#install.packages('ggplot2')
library(ggplot2)
#install.packages('caret')
library(caret)
#install.packages('caretEnsemble')
library(caretEnsemble)
#install.packages('psych')
library(psych)
#install.packages('Amelia')
library(Amelia)
#install.packages('mice')
library(mice)
#install.packages('GGally')
library(GGally)
library(e1071)

setwd("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/code/NB&SVM")

## load in the documents (the corpus)
NovelsCorpus <- Corpus(DirSource("environment"))
(ndocs<-length(NovelsCorpus))
##------------
## OK - now we have both datasets read in. 
## For the text corpus, we need to do a few things.....
##------------
##The following will show you that you read in all the documents
(summary(NovelsCorpus))  ## This will list the docs in the corpus

###################################################################
#######       Change the COrpus into a DTM, a DF, and  Matrix
#######
####################################################################
## There are OPTIONS. This is NOT what you should do - but rather
## things you can do, consider, and learn more about.

# You can ignore extremely rare words i.e. terms that appear in less
# then 1% of the documents. The following is an EXAMPLE not a set method
##(minTermFreq <- ndocs * 0.01) ## Because we only have 13 docs - this will not matter
# You can ignore overly common words i.e. terms that appear in more than
## 50% of the documents
##(maxTermFreq <- ndocs * .50)

## You can create your own Stopwords
## A Wordcloud is good to determine
## if there are odd words you want to remove
#(STOPS <- c("aaron","maggi", "maggie", "philip", "tom", "glegg", "deane", "stephen","tulliver"))

Novels_dtm <- DocumentTermMatrix(NovelsCorpus,
                                 control = list(
                                   #stopwords = TRUE, ## remove normal stopwords
                                   wordLengths=c(4, 8), ## get rid of words of len 3 or smaller or larger than 15
                                   removePunctuation = TRUE,
                                   removeNumbers = TRUE,
                                   tolower=TRUE,
                                   #stemming = TRUE,
                                   remove_separators = TRUE
                                   #stopwords = MyStopwords,
                                   
                                   #removeWords(MyStopwords),
                                   #bounds = list(global = c(minTermFreq, maxTermFreq))
                                 ))
########################################################
################### Have a look #######################
################## and create formats #################
########################################################
#(inspect(Novels_dtm))  ## This takes a look at a subset - a peak
DTM_mat <- as.matrix(Novels_dtm)
(DTM_mat[1:11,1:10])

#########################################################
######### OK - Pause - now the data is vectorized ######
## Its current formats are:
## (1) Novels_dtm is a DocumentTermMatrix R object
## (2) DTM_mat is a matrix
#########################################################

#Novels_dtm <- weightTfIdf(Novels_dtm, normalize = TRUE)
#Novels_dtm <- weightTfIdf(Novels_dtm, normalize = FALSE)

## Look at word freuqncies out of interest
(WordFreq <- colSums(as.matrix(Novels_dtm)))

(head(WordFreq))
(length(WordFreq))
ord <- order(WordFreq)
(WordFreq[head(ord)])
(WordFreq[tail(ord)])
## Row Sums
(Row_Sum_Per_doc <- rowSums((as.matrix(Novels_dtm))))


##################################################################
###############   Convert to dataframe     #######################
##################################################################

## It is important to be able to convert between format.
## Different models require or use different formats.
## First - you can convert a DTM object into a DF...

Novels_DF <- as.data.frame(as.matrix(Novels_dtm))
(Novels_DF[1:11, 1:4])
#(head(Novels_DF))
str(Novels_DF)
(Novels_DF$already)
(nrow(Novels_DF)) 
###############################################################
##
##                         NAIVE BAYES
##
###############################################################
Novels_DF['label']=c('environment',"policy","policy",'environment','environment',"policy",'environment','environment',"policy",'environment','environment','policy',"policy","policy",'environment',"policy","policy",'environment',"policy",'environment','environment',"policy")
Labeled_DF_Novels = Novels_DF

##########################################################
##
##  Create the Testing and Training Sets         
##
########################################################
#####################################################
##        Grabbing Every X value  ##################
####################################################
## 
## This method works whether the data is in order or not.
X = 3   ## This will create a 1/3, 2/3 split. 
## Of course, X can be any number.
(every_X_index<-seq(1,nrow(Labeled_DF_Novels),X))

## Use these X indices to make the Testing and then
## Training sets:

DF_Test<-Labeled_DF_Novels[every_X_index, ]
DF_Train<-Labeled_DF_Novels[-every_X_index, ]
## View the created Test and Train sets
(DF_Test[1:5, 1:5])
(DF_Train[1:5, 1:5])

## Remove and KEEP the label from the test & train sets.
## Make sure label is factor type
DF_Test$label = as.factor(DF_Test$label)
DF_Train$label = as.factor(DF_Train$label)
str(DF_Train$label)  ## GOOD! also type FACTOR
str(DF_Test$label)## Notice that the label is called "label" and is correctly set to type FACTOR. This is IMPORTANT!!

## Copy the Labels
(DF_Test_Labels <- DF_Test$label)
str(DF_Test_Labels)
## Remove the labels
DF_Test_NL<-DF_Test[ , -which(names(DF_Test) %in% c("label"))]
(DF_Test[1:5, 1:5])

## REMOVE THE LABEL FROM THE TRAINING SET...
DF_Train_Labels<-DF_Train$label
DF_Train_NL<-DF_Train[ , -which(names(DF_Train) %in% c("label"))]
(DF_Train_NL[1:5, 1:5])

NB_e1071_2<-naiveBayes(DF_Train_NL, DF_Train_Labels, laplace = 1)
NB_e1071_Pred <- predict(NB_e1071_2, DF_Test_NL)
#NB_e1071_2
table(NB_e1071_Pred,DF_Test_Labels)
(NB_e1071_Pred)

##Visualize
plot(NB_e1071_Pred,col="dark red")

###############################################################
##
##                         SVM
##
###############################################################
SVM_e1071_2<-svm(DF_Train_NL, DF_Train_Labels, kernel="sigmoid", cost=.2, 
                 scale=FALSE)
SVM_e1071_Pred <- predict(SVM_e1071_2, DF_Test_NL)
table(SVM_e1071_Pred,DF_Test_Labels)
(SVM_e1071_Pred)

##Visualize
plot(SVM_e1071_Pred,col=c("dark red","pink"))
