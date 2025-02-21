import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalysis:

    def __init__(self, df):
        self.df = df

    def outliers(self):
        # Visualize the data to check for outliers
        plt.figure(figsize=(12, 6))
        sns.boxplot(y=self.df['Price'])
        plt.title('Boxplot of Prices',fontsize=14, fontweight="bold")
        plt.ylabel('Price',fontsize=14, fontweight="bold")
        plt.show()
    
    def distribution(self):
        #Check for distribution of 'Price'
        fig,axis = plt.subplots(figsize=(12,6))
        sns.histplot(self.df['Price'], kde=True, ax=axis)
        plt.title('Price Distribution',fontsize=14, fontweight="bold")
        plt.xlabel('Price',fontsize=14, fontweight="bold")
        plt.ylabel('Count',fontsize=14, fontweight="bold")
    
    def price_overtime(self):
        #Plot the 'Price' against the 'Date'
        fig = plt.subplots(figsize=(14,8))
        plt.plot(self.df['Price']) 
        plt.title('Brent Oil Prices Over Time',fontsize=14, fontweight="bold")
        plt.xlabel('Year',fontsize=14, fontweight="bold")
        plt.ylabel('Price',fontsize=14, fontweight="bold")