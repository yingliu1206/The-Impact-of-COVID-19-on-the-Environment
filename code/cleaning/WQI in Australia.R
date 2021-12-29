# Load the required packages. 
install.packages("readxl")
library("readxl")

## Jan
# Convert the input xlsx file to a data frame. 
exceldata = read_excel("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/Australia-water-quality-performance-results-january-2020.xlsx")
WQI = data.frame(exceldata)
(head(WQI, n=5)) 

# Look at the data types for the variables in the dataset and correct them
str(WQI)

# Change the data types for the variables and update the dataset
WQI$Average.Value=as.numeric(WQI$Average.Value)

# get the mean of pH in Australia
df_AU1<-WQI[(WQI$Parameter=="pH"),]
a1 = mean(df_AU1$Average.Value, na.rm = TRUE)
# get the mean of Alkalinity in Australia
df_AU2<-WQI[(WQI$Parameter=="Alkalinity"),]
a2 = mean(df_AU2[["Average.Value"]], na.rm = TRUE)
# get the mean of Iron in Australia
df_AU3<-WQI[(WQI$Parameter=="Iron"),]
a3 = mean(df_AU3[["Average.Value"]], na.rm = TRUE)
# get the mean of Calcium in Australia
df_AU4<-WQI[(WQI$Parameter=="Calcium"),]
a4 = mean(df_AU4[["Average.Value"]], na.rm = TRUE)
# get the mean of Magnesium in Australia
df_AU5<-WQI[(WQI$Parameter=="Magnesium"),]
a5 = mean(df_AU5[["Average.Value"]], na.rm = TRUE)
# get the mean of Chloride in Australia
df_AU6<-WQI[(WQI$Parameter=="Chloride"),]
a6 = mean(df_AU6[["Average.Value"]], na.rm = TRUE)

# Create a dataframe of AU_Jan 
df_AU_Jan <- data.frame(country = 'Australia',
                        date = "Jan 2020",
                        pH= a1,
                        Alkalinity = a2,
                        Iron = a3,
                        Calcium = a4,
                        Magnesium = a5,
                        Chloride = a6
)
print (df_AU_Jan)

## Feb
# Convert the input xlsx file to a data frame. 
exceldata2 = read_excel("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/Australia-water-quality-performance-results-february-2020.xlsx")
WQI2 = data.frame(exceldata2)
(head(WQI2, n=5)) 

# Look at the data types for the variables in the dataset and correct them
str(WQI2)

# Change the data types for the variables and update the dataset
WQI2$Average.Value=as.numeric(WQI2$Average.Value)

# get the mean of pH in Australia
df_AU1<-WQI2[(WQI2$Parameter=="pH"),]
a1 = mean(df_AU1$Average.Value, na.rm = TRUE)
# get the mean of Alkalinity in Australia
df_AU2<-WQI2[(WQI2$Parameter=="Alkalinity"),]
a2 = mean(df_AU2[["Average.Value"]], na.rm = TRUE)
# get the mean of Iron in Australia
df_AU3<-WQI2[(WQI2$Parameter=="Iron"),]
a3 = mean(df_AU3[["Average.Value"]], na.rm = TRUE)
# get the mean of Calcium in Australia
df_AU4<-WQI2[(WQI2$Parameter=="Calcium"),]
a4 = mean(df_AU4[["Average.Value"]], na.rm = TRUE)
# get the mean of Magnesium in Australia
df_AU5<-WQI2[(WQI2$Parameter=="Magnesium"),]
a5 = mean(df_AU5[["Average.Value"]], na.rm = TRUE)
# get the mean of Chloride in Australia
df_AU6<-WQI2[(WQI2$Parameter=="Chloride"),]
a6 = mean(df_AU6[["Average.Value"]], na.rm = TRUE)

# Create a dataframe of AU_Feb 
df_AU_Feb <- data.frame(country = 'Australia',
                        date = "Feb 2020",
                        pH= a1,
                        Alkalinity = a2,
                        Iron = a3,
                        Calcium = a4,
                        Magnesium = a5,
                        Chloride = a6
)
print (df_AU_Feb)

## March
# Convert the input xlsx file to a data frame. 
exceldata3 = read_excel("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/Australia-water-quality-performance-results-march-2020.xlsx")
WQI3 = data.frame(exceldata3)
(head(WQI3, n=5)) 

# Look at the data types for the variables in the dataset and correct them
str(WQI3)

# Change the data types for the variables and update the dataset
WQI3$Average.Value=as.numeric(WQI3$Average.Value)

# get the mean of pH in Australia
df_AU1<-WQI3[(WQI3$Parameter=="pH"),]
a1 = mean(df_AU1$Average.Value, na.rm = TRUE)
# get the mean of Alkalinity in Australia
df_AU2<-WQI3[(WQI3$Parameter=="Alkalinity"),]
a2 = mean(df_AU2[["Average.Value"]], na.rm = TRUE)
# get the mean of Iron in Australia
df_AU3<-WQI3[(WQI3$Parameter=="Iron"),]
a3 = mean(df_AU3[["Average.Value"]], na.rm = TRUE)
# get the mean of Calcium in Australia
df_AU4<-WQI3[(WQI3$Parameter=="Calcium"),]
a4 = mean(df_AU4[["Average.Value"]], na.rm = TRUE)
# get the mean of Magnesium in Australia
df_AU5<-WQI3[(WQI3$Parameter=="Magnesium"),]
a5 = mean(df_AU5[["Average.Value"]], na.rm = TRUE)
# get the mean of Chloride in Australia
df_AU6<-WQI3[(WQI3$Parameter=="Chloride"),]
a6 = mean(df_AU6[["Average.Value"]], na.rm = TRUE)

# Create a dataframe of AU_Mar 
df_AU_Mar <- data.frame(country = 'Australia',
                        date = "March 2020",
                        pH= a1,
                        Alkalinity = a2,
                        Iron = a3,
                        Calcium = a4,
                        Magnesium = a5,
                        Chloride = a6
)
print (df_AU_Mar)

## April
# Convert the input xlsx file to a data frame. 
exceldata4 = read_excel("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/Australia-water-quality-performance-results-april-2020.xlsx")
WQI4 = data.frame(exceldata4)
(head(WQI4, n=5)) 

# Look at the data types for the variables in the dataset and correct them
str(WQI4)

# Change the data types for the variables and update the dataset
WQI4$Average.Value=as.numeric(WQI4$Average.Value)

# get the mean of pH in Australia
df_AU1<-WQI4[(WQI4$Parameter=="pH"),]
a1 = mean(df_AU1$Average.Value, na.rm = TRUE)
# get the mean of Alkalinity in Australia
df_AU2<-WQI4[(WQI4$Parameter=="Alkalinity"),]
a2 = mean(df_AU2[["Average.Value"]], na.rm = TRUE)
# get the mean of Iron in Australia
df_AU3<-WQI4[(WQI4$Parameter=="Iron"),]
a3 = mean(df_AU3[["Average.Value"]], na.rm = TRUE)
# get the mean of Calcium in Australia
df_AU4<-WQI4[(WQI4$Parameter=="Calcium"),]
a4 = mean(df_AU4[["Average.Value"]], na.rm = TRUE)
# get the mean of Magnesium in Australia
df_AU5<-WQI4[(WQI4$Parameter=="Magnesium"),]
a5 = mean(df_AU5[["Average.Value"]], na.rm = TRUE)
# get the mean of Chloride in Australia
df_AU6<-WQI4[(WQI4$Parameter=="Chloride"),]
a6 = mean(df_AU6[["Average.Value"]], na.rm = TRUE)

# Create a dataframe of AU_Apr 
df_AU_Apr <- data.frame(country = 'Australia',
                        date = "April 2020",
                        pH= a1,
                        Alkalinity = a2,
                        Iron = a3,
                        Calcium = a4,
                        Magnesium = a5,
                        Chloride = a6
)
print (df_AU_Apr)

## May
# Convert the input xlsx file to a data frame. 
exceldata5 = read_excel("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/Austrlia-water-quality-performance-results-may-2020.xlsx")
WQI5 = data.frame(exceldata5)
(head(WQI5, n=5)) 

# Look at the data types for the variables in the dataset and correct them
str(WQI5)

# Change the data types for the variables and update the dataset
WQI5$Average.Value=as.numeric(WQI5$Average.Value)

# get the mean of pH in Australia
df_AU1<-WQI5[(WQI5$Parameter=="pH"),]
a1 = mean(df_AU1$Average.Value, na.rm = TRUE)
# get the mean of Alkalinity in Australia
df_AU2<-WQI5[(WQI5$Parameter=="Alkalinity"),]
a2 = mean(df_AU2[["Average.Value"]], na.rm = TRUE)
# get the mean of Iron in Australia
df_AU3<-WQI5[(WQI5$Parameter=="Iron"),]
a3 = mean(df_AU3[["Average.Value"]], na.rm = TRUE)
# get the mean of Calcium in Australia
df_AU4<-WQI5[(WQI5$Parameter=="Calcium"),]
a4 = mean(df_AU4[["Average.Value"]], na.rm = TRUE)
# get the mean of Magnesium in Australia
df_AU5<-WQI5[(WQI5$Parameter=="Magnesium"),]
a5 = mean(df_AU5[["Average.Value"]], na.rm = TRUE)
# get the mean of Chloride in Australia
df_AU6<-WQI5[(WQI5$Parameter=="Chloride"),]
a6 = mean(df_AU6[["Average.Value"]], na.rm = TRUE)

# Create a dataframe of AU_May 
df_AU_May <- data.frame(country = 'Australia',
                        date = "May 2020",
                        pH= a1,
                        Alkalinity = a2,
                        Iron = a3,
                        Calcium = a4,
                        Magnesium = a5,
                        Chloride = a6
)
print (df_AU_May)

## June
# Convert the input xlsx file to a data frame. 
exceldata6 = read_excel("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/Australia-water-quality-performance-results-june-2020.xlsx")
WQI6 = data.frame(exceldata6)
(head(WQI6, n=5)) 

# Look at the data types for the variables in the dataset and correct them
str(WQI6)

# Change the data types for the variables and update the dataset
WQI6$Average.Value=as.numeric(WQI6$Average.Value)

# get the mean of pH in Australia
df_AU1<-WQI6[(WQI6$Parameter=="pH"),]
a1 = mean(df_AU1$Average.Value, na.rm = TRUE)
# get the mean of Alkalinity in Australia
df_AU2<-WQI6[(WQI6$Parameter=="Alkalinity"),]
a2 = mean(df_AU2[["Average.Value"]], na.rm = TRUE)
# get the mean of Iron in Australia
df_AU3<-WQI6[(WQI6$Parameter=="Iron"),]
a3 = mean(df_AU3[["Average.Value"]], na.rm = TRUE)
# get the mean of Calcium in Australia
df_AU4<-WQI6[(WQI6$Parameter=="Calcium"),]
a4 = mean(df_AU4[["Average.Value"]], na.rm = TRUE)
# get the mean of Magnesium in Australia
df_AU5<-WQI6[(WQI6$Parameter=="Magnesium"),]
a5 = mean(df_AU5[["Average.Value"]], na.rm = TRUE)
# get the mean of Chloride in Australia
df_AU6<-WQI6[(WQI6$Parameter=="Chloride"),]
a6 = mean(df_AU6[["Average.Value"]], na.rm = TRUE)

# Create a dataframe of AU_Jun 
df_AU_Jun <- data.frame(country = 'Australia',
                        date = "June 2020",
                        pH= a1,
                        Alkalinity = a2,
                        Iron = a3,
                        Calcium = a4,
                        Magnesium = a5,
                        Chloride = a6
)
print (df_AU_Jun)

## July
# Convert the input xlsx file to a data frame. 
exceldata7 = read_excel("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/Australia-water-quality-performance-results-july-2020.xlsx")
WQI7 = data.frame(exceldata7)
(head(WQI7, n=5)) 

# Look at the data types for the variables in the dataset and correct them
str(WQI7)

# Change the data types for the variables and update the dataset
WQI7$Average.Value=as.numeric(WQI7$Average.Value)

# get the mean of pH in Australia
df_AU1<-WQI7[(WQI7$Parameter=="pH"),]
a1 = mean(df_AU1$Average.Value, na.rm = TRUE)
# get the mean of Alkalinity in Australia
df_AU2<-WQI7[(WQI7$Parameter=="Alkalinity"),]
a2 = mean(df_AU2[["Average.Value"]], na.rm = TRUE)
# get the mean of Iron in Australia
df_AU3<-WQI7[(WQI7$Parameter=="Iron"),]
a3 = mean(df_AU3[["Average.Value"]], na.rm = TRUE)
# get the mean of Calcium in Australia
df_AU4<-WQI7[(WQI7$Parameter=="Calcium"),]
a4 = mean(df_AU4[["Average.Value"]], na.rm = TRUE)
# get the mean of Magnesium in Australia
df_AU5<-WQI7[(WQI7$Parameter=="Magnesium"),]
a5 = mean(df_AU5[["Average.Value"]], na.rm = TRUE)
# get the mean of Chloride in Australia
df_AU6<-WQI7[(WQI7$Parameter=="Chloride"),]
a6 = mean(df_AU6[["Average.Value"]], na.rm = TRUE)

# Create a dataframe of AU_Jul 
df_AU_Jul <- data.frame(country = 'Australia',
                        date = "July 2020",
                        pH= a1,
                        Alkalinity = a2,
                        Iron = a3,
                        Calcium = a4,
                        Magnesium = a5,
                        Chloride = a6
)
print (df_AU_Jul)

# combine dataframes
WQIAustralia <- rbind(df_AU_Jan, df_AU_Feb, df_AU_Mar, df_AU_Apr, df_AU_May, df_AU_Jun, df_AU_Jul)
WQIAustralia

file = "/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/WQIAustralia.csv"
write.csv(WQIAustralia, file, row.names = FALSE)

# Draw
ggplot(WQIAustralia, aes(x=date, y=pH)) + 
  geom_bar(stat = "identity", width=0.5) 

ggplot(WQIAustralia, aes(x=date, y=Alkalinity)) + 
  geom_bar(stat = "identity", width=0.5) 

ggplot(WQIAustralia, aes(x=date, y=Iron)) + 
  geom_bar(stat = "identity", width=0.5) 

ggplot(WQIAustralia, aes(x=date, y=Calcium)) + 
  geom_bar(stat = "identity", width=0.5) 

ggplot(WQIAustralia, aes(x=date, y=Magnesium)) + 
  geom_bar(stat = "identity", width=0.5) 

ggplot(WQIAustralia, aes(x=date, y=Chloride)) + 
  geom_bar(stat = "identity", width=0.5) 