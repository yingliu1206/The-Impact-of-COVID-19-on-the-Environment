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

# find outliers
x <- COVID19$DeathsSum
y <- COVID19$ConfirmedSum
# Plot with main and axis titles
# Change point shape (pch = 19) and remove frame.
plot(x, y, main = "ConfirmedSum&DeathsSum",
     xlab = "DeathsSum", ylab = "ConfirmedSum",
     pch = 19, frame = FALSE)

# Add regression line
plot(x, y, main = "ConfirmedSum&DeathsSum",
     xlab = "DeathsSum", ylab = "ConfirmedSum",
     pch = 19, frame = FALSE)
abline(lm(y ~ x, data = mtcars), col = "blue")

x <- COVID19$RecoveredSum
y <- COVID19$ConfirmedSum
# Plot with main and axis titles
# Change point shape (pch = 19) and remove frame.
plot(x, y, main = "RecoveredSum&ConfirmedSum",
     xlab = "RecoveredSum", ylab = "ConfirmedSum",
     pch = 19, frame = FALSE)

# Add regression line
plot(x, y, main = "RecoveredSum&ConfirmedSum",
     xlab = "RecoveredSum", ylab = "ConfirmedSum",
     pch = 19, frame = FALSE)
abline(lm(y ~ x, data = mtcars), col = "blue")

# select covid-19 data of five countries
rownames(COVID19) = COVID19$Countries
COVID19_five = COVID19[c('Australia','China','Ethiopia','US','United Kingdom'),]
COVID19_five

# find outliers
x <- COVID19_five$DeathsSum
y <- COVID19_five$ConfirmedSum
# Plot with main and axis titles
# Change point shape (pch = 19) and remove frame.
plot(x, y, main = "ConfirmedSum&DeathsSum",
     xlab = "DeathsSum", ylab = "ConfirmedSum",
     pch = 19, frame = FALSE)

# Add regression line
plot(x, y, main = "ConfirmedSum&DeathsSum",
     xlab = "DeathsSum", ylab = "ConfirmedSum",
     pch = 19, frame = FALSE)
abline(lm(y ~ x, data = mtcars), col = "blue")

x <- COVID19_five$RecoveredSum
y <- COVID19_five$ConfirmedSum
# Plot with main and axis titles
# Change point shape (pch = 19) and remove frame.
plot(x, y, main = "RecoveredSum&ConfirmedSum",
     xlab = "RecoveredSum", ylab = "ConfirmedSum",
     pch = 19, frame = FALSE)

# Add regression line
plot(x, y, main = "RecoveredSum&ConfirmedSum",
     xlab = "RecoveredSum", ylab = "ConfirmedSum",
     pch = 19, frame = FALSE)
abline(lm(y ~ x, data = mtcars), col = "blue")
