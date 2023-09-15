import csv
import pandas as pd

class CsvHelper:

    def __init__(self, names):
        self.names = names
    
    def CreateGainLossCsv(self, analysis):
        self.analysis = analysis
        data_header = ['Name', 'Initial Share Cost', 'Share Cost', 'Initial Worth', 'Worth', 'GainedTotal', 'GainedPercent']
        data = []
        for stock in self.analysis.stocks:
            stockInfo = []
            stockInfo.append(stock.name)
            stockInfo.append(stock.boughtStockPrice)
            stockInfo.append(stock.currentStockPrice)
            stockInfo.append(stock.boughtStockWorth)
            stockInfo.append(stock.currentStockWorth)
            stockInfo.append(stock.gainLossPrice)
            stockInfo.append(stock.gainLossPercent)
            data.append(stockInfo)

        fileName = "Reports/Profile/StocksGainLoss.csv"
        with open(fileName, 'w') as file_writer:
            writer = csv.writer(file_writer)
            writer.writerow(data_header)
            for item in data:
                writer.writerow(item)

        self.RemoveEmptyRows(fileName) 


    def CreateStockReportCsv(self, name, history, span, interval):
        data_header = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        data = []
        for info in history:
            stockInfo = []
            stockInfo.append(info["begins_at"])
            stockInfo.append(info["open_price"])
            stockInfo.append(info["high_price"])
            stockInfo.append(info["low_price"])
            stockInfo.append(info["close_price"])
            stockInfo.append(info["volume"])
            data.append(stockInfo)
        fileName = "Reports/History/{}-{}-{}.csv".format(name, span, interval)

        with open(fileName, 'w') as file_writer:
            writer = csv.writer(file_writer)
            writer.writerow(data_header)
            for item in data:
                writer.writerow(item)

        self.RemoveEmptyRows(fileName)  

    def RemoveEmptyRows(self, fileName):
        file = pd.read_csv(fileName)
        file.to_csv(fileName, index=False)

    
