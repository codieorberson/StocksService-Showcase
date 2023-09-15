
import json
from Services.StockAnalysisService import StockAnalysis
from Models.ProfileOverview import ProfileOverview
class StocksAnalyses:

    def __init__(self, stockNames):
        print("StocksAnalyses.Init")
        self.stocks = []
        self.stockNames = stockNames
        self.SetStocks()
        self.SetGainLossTotal()
        self.SetTotalInvested()
        self.SetGainLossPercent()
        self.SetTotalWorth()

    def GetOverview(self):
        overview = ProfileOverview()
        overview.SetFields(self.totalGainLoss, self.gainLossPercent, self.totalInvested, self.totalWorth)
        return json.dumps(overview.__dict__)
    
    def GetDetailedOverview(self):
        detailedInfo = {}
        for stockName in self.stockNames:
            stockInfo = StockAnalysis(stockName)
            detailedInfo[stockName] = stockInfo()
        return detailedInfo
    
    def SetStocks(self):
        for stockName in self.stockNames:
            self.stocks.append(StockAnalysis(stockName))
        
    def SetGainLossTotal(self):
        self.totalGainLoss = 0
        for stock in self.stocks:
            self.totalGainLoss += stock.gainLossPrice

    def SetGainLossPercent(self):
        self.gainLossPercent = float(self.totalGainLoss) / float(self.totalInvested)

    def SetTotalInvested(self):
        self.totalInvested = 0
        for stock in self.stocks:
            self.totalInvested += stock.boughtStockWorth
    
    def SetTotalWorth(self):
        self.totalWorth = 0
        for stock in self.stocks:
            self.totalWorth += stock.currentStockWorth

    

    
    