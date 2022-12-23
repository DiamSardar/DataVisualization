# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reading file using pandas
data = pd.read_csv("C:\\Users\\RajaI\\Desktop\\Cost_of_Living_Index_2022.csv")
print(data)


# Line graph visualisation
def LineGraph(data):
    '''
    Function to plot line graph to show rent, Local Purchasing Power Index
    and restaurant index of different countries
    '''
    # Selecting last 8 countries of dataset
    data = data.tail(8)
    data.plot(x="Country", y=["Rent Index", "Groceries Index",
                              "Local Purchasing Power Index"], kind='line')
    plt.xlabel("Country")
    plt.ylabel("Cost of Living")
    plt.title('Line Graph')
    plt.legend(loc="upper right")
    plt.xticks(rotation=90)
    plt.show()


# Bar graph visualisation
def Bargraph(data):
    '''
    Function to plot bargraph to showrent and groceries index of 5
    countries
    '''
# Selecting first 7 countries of dataset
    data = data.head(7)
    data.plot(x="Country", y=["Rent Index", "Groceries Index"], kind='barh')
    plt.ylabel("Country")
    plt.xlabel("Cost of Living")
    plt.title('Bar Graph')
    plt.xticks(rotation=90)
    plt.show()


# Scatter plot visualisation
def ScatterPlot(data):
    '''
    Function to visualise scatter plot to show  relationship of rent and
    restaurant index of different countries
    '''
    plt.scatter(data['Rent Index'], data['Cost of Living Index'], color='blue',
                marker='^')
    plt.xlabel("Rent Index")
    plt.ylabel("Cost of Living")
    plt.title('Scatter Plot')
    plt.xticks(rotation=90)
    plt.show


# Function Call
LineGraph(data)
Bargraph(data)
ScatterPlot(data)
