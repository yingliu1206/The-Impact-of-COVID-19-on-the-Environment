# Read csv file with baby names and make new column names
COVID19 = read.csv("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/COVID19.csv", header=FALSE, stringsAsFactors=FALSE)
names(COVID19) = c("Countries", "Confirmed","Deaths","Recovered", "Active","New cases","New deaths", "New recovered","Deaths / 100 Cases","Recovered / 100 Cases","Deaths / 100 Recovered", "Confirmed last week", "1 week change", "1 week % increase","WHO Region")
(head(COVID19, n=5)) 

# delete the first row
COVID19 <- COVID19[-1,]

# Look at the data types for the variables in the dataset and correct them
str(COVID19)
## Change the data types for the variables and update the dataset
COVID19$Confirmed=as.numeric(COVID19$Confirmed)
COVID19$Deaths=as.numeric(COVID19$Deaths)
COVID19$Recovered=as.numeric(COVID19$Recovered) 
COVID19$`New cases`=as.numeric(COVID19$`New cases`)
COVID19$`New deaths`=as.numeric(COVID19$`New deaths`)
COVID19$`New recovered`=as.numeric(COVID19$`New recovered`)
COVID19$`Confirmed last week`=as.numeric(COVID19$`Confirmed last week`)
COVID19$`1 week % increase`=as.numeric(COVID19$`1 week % increase`)

str(COVID19)

# Aggregate relevant columns
COVID19$ConfirmedSum = COVID19$Confirmed + COVID19$`New cases` + COVID19$`Confirmed last week` 
COVID19$DeathsSum = COVID19$Deaths + COVID19$`New deaths` 
COVID19$RecoveredSum = COVID19$Recovered + COVID19$`New recovered` 

# remove irrelevant columns
COVID19= subset(COVID19, select = -c(Confirmed, Deaths, Recovered, `New cases`, `Confirmed last week`, `New deaths`, `New recovered`, Active, `Deaths / 100 Cases`, `Recovered / 100 Cases`, `Deaths / 100 Recovered`, `1 week change`))
(head(COVID19, n=5)) 

# Delete all rows that contain NA values
COVID19 = COVID19[complete.cases(COVID19),]

# find covid-19 data of five countries
rownames(COVID19) = COVID19$Countries
COVID19_five = COVID19[c('Australia','China','Egypt','US','United Kingdom'),]
COVID19_five

# Discretization
library(dplyr)

# 1. COVID19 dataset
(confirmed_mean = mean(COVID19_five$ConfirmedSum))
(covid_d = transmute(COVID19_five, 
          covid19_cat = ifelse(ConfirmedSum < confirmed_mean, "covid19 below average", "covid19 at or above average")))

# 2. AQI dataset
(AQI = read.csv("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/airqualityNew.csv"))
(pm2.5_mean = mean(AQI$pm2.5))
(aqi_d = transmute(AQI, 
                   aqi_cat = ifelse(pm2.5 < pm2.5_mean, "AQI below average", "AQI at or above average")))
# 3. Weather dataset
(Weather = read.csv("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/weatherNew.csv"))
(windgust_mean = mean(Weather$windgust))
(weather_d = transmute(Weather, 
                   weather_cat = ifelse(windgust < windgust_mean, "windgust below average", "windgust at or above average")))

# 4. WQI dataset
(WQI = read.csv("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/WQINew.csv"))
(pH_mean = mean(WQI$pH))
(wqi_d = transmute(WQI, 
                   wqi_cat = ifelse(pH < pH_mean, "WQI below average", "WQI at or above average")))
str(wqi_d)

# combine dataframes
(ARM_environment <- cbind(a = c(1:5), covid_d, aqi_d, weather_d, wqi_d))
(names(ARM_environment) <- NULL) # remove column names

# save as a csv file
file = "/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/ARM_environment.csv"
write.csv(ARM_environment, file, row.names = FALSE)

