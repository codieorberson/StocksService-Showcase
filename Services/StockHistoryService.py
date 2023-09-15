
import yfinance as yf
from Models.StockHistoryModel import StockHistoryModel
import pandas as pd
from datetime import datetime, timedelta
class StockHistory:

    def GetStockPriceHistory(self, name, period='1d', interval='max'):
        priceHistory = yf.Ticker(name).history(period, interval, actions=False)
        print(priceHistory)

    def GetStocksPriceHistory(self, names, period, interval):
        stocksHistory = []
        for name in names:
            history = yf.Ticker(name).history(period, interval, actions=False, rounding=True)
            stockHistoryModel = StockHistoryModel()
            stockHistoryModel.Name = name
            stockHistoryModel.Opens = list(history['Open'])
            stockHistoryModel.Highs = list(history['High'])
            stockHistoryModel.Lows = list(history['Low'])
            stockHistoryModel.Closes = list(history['Close'])
            stockHistoryModel.Volumes = list(history['Volume'])
            stockDates = list()
            for stockindex in history.index:
                stockDate = datetime.fromtimestamp((stockindex.value //1e9)).strftime('%Y-%m-%d %H:%M:%S')
                stockDates.append(stockDate)
            stockHistoryModel.Dates = stockDates
            stocksHistory.append(stockHistoryModel)
        return(stocksHistory)
           
    def GetPriceHistoryByRange(self, name, startDate, endDate):
        stocksHistory = []
        startDate = datetime.strptime(startDate[:10], "%Y-%m-%d")
        endDate = datetime.strptime(endDate[:10], "%Y-%m-%d")
        currDate = startDate
        history = pd.DataFrame()

        while currDate < endDate:
            nextMonth = currDate + timedelta(days=30) 
            if nextMonth > endDate:
                nextMonth = endDate

            monthData = yf.Ticker(name).history(start=currDate.strftime("%Y-%m-%d"), 
                                                 end=nextMonth.strftime("%Y-%m-%d"), 
                                                 actions=False, 
                                                 rounding=True)
            history = pd.concat([history, monthData])

            currDate = nextMonth

            stockDates = list()
            for stockindex in history.index:
                stockDate = datetime.fromtimestamp((stockindex.value //1e9)).strftime('%Y-%m-%d')
                stockDates.append(stockDate)
            stockHistoryModel = StockHistoryModel()
            dates = stockDates
            stockHistoryModel.SetFields(name,
                                        dates,
                                        list(history['Open']),
                                        list(history['High']),
                                        list(history['Low']),
                                        list(history['Close']),
                                        list(history['Volume'])
            )
            
            for i in range(len(stockHistoryModel.Dates)):
                sh = StockHistoryModel()
                sh.SetFields(name,
                            stockHistoryModel.Dates[i],  
                            stockHistoryModel.Opens[i],  
                            stockHistoryModel.Highs[i], 
                            stockHistoryModel.Lows[i],  
                            stockHistoryModel.Closes[i],  
                            stockHistoryModel.Volumes[i],    
                )
                stocksHistory.append(sh)
        
        return(self.RemoveDuplicates(stocksHistory))

    def RemoveDuplicates(self, stocks):
        seenDates = set()
        dedupedStockNewsList = []
        for item in stocks:
            if item.Dates not in seenDates:
                seenDates.add(item.Dates)
                dedupedStockNewsList.append(item)
        stockNewsList = dedupedStockNewsList
        return stockNewsList


    
    
