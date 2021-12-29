# Read csv file with baby names and make new column names
airquality = read.csv("/Users/LiuYing/Desktop/GU/2020-fall/ANLY-501-01/dataset/data/airquality.csv", header=FALSE, stringsAsFactors=FALSE)
names(airquality) = c("Date", "Country","City","Specie", "count","min","max", "median","variance")
(head(airquality, n=5)) 

# delete the first row
airquality <- airquality[-1,]

# Look at the data types for the variables in the dataset and correct them
str(airquality)

## Change the data types for the variables and update the dataset
airquality$count=as.numeric(airquality$count)
airquality$min=as.numeric(airquality$min)
airquality$max=as.numeric(airquality$max)
airquality$median=as.numeric(airquality$median)
airquality$variance=as.numeric(airquality$variance)

# select AQI data of five countries
airquality<-airquality[(airquality$Country=="AU" | airquality$Country=="CN" | airquality$Country=="ET" | airquality$Country=="GB" | airquality$Country=="MX"),]
airquality

# get the mean of pm2.5 in Australia
df_AU1<-airquality[(airquality$Country=="AU" | airquality$Specie=="pm25"),]
a1 = mean(df_AU1[["count"]])
# get the mean of pm10 in Australia
df_AU2<-airquality[(airquality$Country=="AU" | airquality$Specie=="pm10"),]
a2 = mean(df_AU2[["count"]])
# get the mean of co in Australia
df_AU3<-airquality[(airquality$Country=="AU" | airquality$Specie=="co"),]
a3 = mean(df_AU3[["count"]])
# get the mean of no2 in Australia
df_AU4<-airquality[(airquality$Country=="AU" | airquality$Specie=="no2"),]
a4 = mean(df_AU4[["count"]])
# get the mean of so2 in Australia
df_AU5<-airquality[(airquality$Country=="AU" | airquality$Specie=="so2"),]
a5 = mean(df_AU5[["count"]])
# get the mean of o3 in Australia
df_AU6<-airquality[(airquality$Country=="AU" | airquality$Specie=="o3"),]
a6 = mean(df_AU6[["count"]])

# Create a dataframe of AU 
df_AU <- data.frame(country = 'Australia',
                    pm2.5= a1,
                    pm10 = a2,
                    co = a3,
                    no2 = a4,
                    so2 = a5,
                    o3 = a6
)
print (df_AU)

# get the mean of pm2.5 in China
df_CN1<-airquality[(airquality$Country=="CN" | airquality$Specie=="pm25"),]
c1 = mean(df_CN1[["count"]])
# get the mean of pm10 in China
df_CN2<-airquality[(airquality$Country=="CN" | airquality$Specie=="pm10"),]
c2 = mean(df_CN2[["count"]])
# get the mean of co in China
df_CN3<-airquality[(airquality$Country=="CN" | airquality$Specie=="co"),]
c3 = mean(df_CN3[["count"]])
# get the mean of no2 in China
df_CN4<-airquality[(airquality$Country=="CN" | airquality$Specie=="no2"),]
c4 = mean(df_CN4[["count"]])
# get the mean of so2 in China
df_CN5<-airquality[(airquality$Country=="CN" | airquality$Specie=="so2"),]
c5 = mean(df_CN5[["count"]])
# get the mean of o3 in China
df_CN6<-airquality[(airquality$Country=="CN" | airquality$Specie=="o3"),]
c6 = mean(df_CN6[["count"]])

# Create a dataframe of CN
df_CN <- data.frame(country = 'China',
                    pm2.5= c1,
                    pm10 = c2,
                    co = c3,
                    no2 = c4,
                    so2 = c5,
                    o3 = c6
)
print (df_CN)

# get the mean of pm2.5 in United Kingdom
df_GB1<-airquality[(airquality$Country=="GB" | airquality$Specie=="pm25"),]
g1 = mean(df_GB1[["count"]])
# get the mean of pm10 in United Kingdom
df_GB2<-airquality[(airquality$Country=="GB" | airquality$Specie=="pm10"),]
g2 = mean(df_GB2[["count"]])
# get the mean of co in United Kingdom
df_GB3<-airquality[(airquality$Country=="GB" | airquality$Specie=="co"),]
g3 = mean(df_GB3[["count"]])
# get the mean of no2 in United Kingdom
df_GB4<-airquality[(airquality$Country=="GB" | airquality$Specie=="no2"),]
g4 = mean(df_GB4[["count"]])
# get the mean of so2 in United Kingdom
df_GB5<-airquality[(airquality$Country=="GB" | airquality$Specie=="so2"),]
g5 = mean(df_GB5[["count"]])
# get the mean of o3 in United Kingdom
df_GB6<-airquality[(airquality$Country=="GB" | airquality$Specie=="o3"),]
g6 = mean(df_GB6[["count"]])

# Create a dataframe of GB
df_GB <- data.frame(country = 'United Kingdom',
                    pm2.5= g1,
                    pm10 = g2,
                    co = g3,
                    no2 = g4,
                    so2 = g5,
                    o3 = g6
)
print (df_GB)

# get the mean of pm2.5 in Ethiopia
df_ET1<-airquality[(airquality$Country=="ET" | airquality$Specie=="pm25"),]
e1 = mean(df_ET1[["count"]])
# get the mean of pm10 in Ethiopia
df_ET2<-airquality[(airquality$Country=="ET" | airquality$Specie=="pm10"),]
e2 = mean(df_ET2[["count"]])
# get the mean of co in Ethiopia
df_ET3<-airquality[(airquality$Country=="ET" | airquality$Specie=="co"),]
e3 = mean(df_ET3[["count"]])
# get the mean of no2 in Ethiopia
df_ET4<-airquality[(airquality$Country=="ET" | airquality$Specie=="no2"),]
e4 = mean(df_ET4[["count"]])
# get the mean of so2 in Ethiopia
df_ET5<-airquality[(airquality$Country=="ET" | airquality$Specie=="so2"),]
e5 = mean(df_ET5[["count"]])
# get the mean of o3 in Ethiopia
df_ET6<-airquality[(airquality$Country=="ET" | airquality$Specie=="o3"),]
e6 = mean(df_ET6[["count"]])

# Create a dataframe of ET
df_ET <- data.frame(country = 'Ethiopia',
                    pm2.5= e1,
                    pm10 = e2,
                    co = e3,
                    no2 = e4,
                    so2 = e5,
                    o3 = e6
)
print (df_ET)

# get the mean of pm2.5 in Mexico
df_MX1<-airquality[(airquality$Country=="MX" | airquality$Specie=="pm25"),]
m1 = mean(df_MX1[["count"]])
# get the mean of pm10 in Mexico
df_MX2<-airquality[(airquality$Country=="MX" | airquality$Specie=="pm10"),]
m2 = mean(df_MX2[["count"]])
# get the mean of co in Mexico
df_MX3<-airquality[(airquality$Country=="MX" | airquality$Specie=="co"),]
m3 = mean(df_MX3[["count"]])
# get the mean of no2 in Mexico
df_MX4<-airquality[(airquality$Country=="MX" | airquality$Specie=="no2"),]
m4 = mean(df_MX4[["count"]])
# get the mean of so2 in Mexico
df_MX5<-airquality[(airquality$Country=="MX" | airquality$Specie=="so2"),]
m5 = mean(df_MX5[["count"]])
# get the mean of o3 in Mexico
df_MX6<-airquality[(airquality$Country=="MX" | airquality$Specie=="o3"),]
m6 = mean(df_MX6[["count"]])

# Create a dataframe of MX
df_MX <- data.frame(country = 'Mexico',
                    pm2.5= m1,
                    pm10 = m2,
                    co = m3,
                    no2 = m4,
                    so2 = m5,
                    o3 = m6
)
print (df_MX)

# combine dataframes
airqualityNew <- rbind(df_AU, df_CN, df_GB, df_ET, df_MX)

# add a date column
airqualityNew$Date = "2020.01-2020.08"
airqualityNew

# find outliers
x <- airqualityNew$pm2.5
y <- airqualityNew$pm10
# Plot with main and axis titles
# Change point shape (pch = 19) and remove frame.
plot(x, y, main = "pm2.5&pm10",
     xlab = "pm2.5", ylab = "pm10",
     pch = 19, frame = FALSE)

# Add regression line
plot(x, y, main = "pm2.5&pm10",
     xlab = "pm2.5", ylab = "pm10",
     pch = 19, frame = FALSE)
abline(lm(y ~ x, data = mtcars), col = "blue")

# find outliers
x <- airqualityNew$co
y <- airqualityNew$no2
# Plot with main and axis titles
# Change point shape (pch = 19) and remove frame.
plot(x, y, main = "co&no2",
     xlab = "co", ylab = "no2",
     pch = 19, frame = FALSE)

# Add regression line
plot(x, y, main = "co&no2",
     xlab = "co", ylab = "no2",
     pch = 19, frame = FALSE)
abline(lm(y ~ x, data = mtcars), col = "blue")

# find outliers
x <- airqualityNew$so2
y <- airqualityNew$o3
# Plot with main and axis titles
# Change point shape (pch = 19) and remove frame.
plot(x, y, main = "so2&o3",
     xlab = "so2", ylab = "o3",
     pch = 19, frame = FALSE)

# Add regression line
plot(x, y, main = "so2&o3",
     xlab = "so2", ylab = "o3",
     pch = 19, frame = FALSE)
abline(lm(y ~ x, data = mtcars), col = "blue")