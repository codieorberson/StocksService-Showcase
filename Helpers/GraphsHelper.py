
import pandas as pd 
import matplotlib.pyplot as plt

class Graphs:

    def __init__(self, csvName):
        self.name = csvName
        self.dataset_test = pd.read_csv(self.name)
        self.stock_price = self.dataset_test.iloc[:,1:2].values

    def DisplayGraph(self):
        plt.plot(self.stock_price, color='red', label='Stock Price')
        plt.title('Stock Price')
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.legend()
        plt.show()

    
    
