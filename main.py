import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

#1.1
# declare our dataframe as df and read the stockprice.csv into our variable so we can call on it throughout the program
df = pd.read_csv('stockprice.csv')
print(df) #Print out our dataframe to display the data

#1.2
#get the highest stock from the amazon data column using the max function and printing our answer
highest_stock = df['Amazon'].max()
print(highest_stock)
#get the lowest stock from the amazon data column using the min function and printing our answer
lowest_stock = df['Amazon'].min()
print(lowest_stock)

#1.3
#get the mean of the google data column by using the mean function and printing our answer
mean = df['Google'].mean()
print(mean)

#get the standard deviation of the google data column by using the std function and printing our answer
standard_deviation = df['Google'].std()
print(standard_deviation)

#get the variance of the google data column by using the var function and printing our answer
variance = df['Google'].var()
print(variance)

#1.4
#Creating our line graph based setting it according to dates as the x axis and y axis as our data columns and making the type of graph a line graph, we then show our graph
df.plot(x='Date', y=['Amazon', 'Google', 'Facebook'], kind='line')
plt.show()

#Creating our bar graph based setting it according to dates as the x axis and y axis as our data columns and making the type of graph a bar graph, we then show our graph
df.plot(x='Date', y=['Amazon', 'Google', 'Facebook'], kind='bar')
plt.show()