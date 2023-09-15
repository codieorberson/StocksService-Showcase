
import numpy as np
# from sklearn.model_selection import train_test_split
# import tensorflow as tf
# from keras.preprocessing.text import Tokenizer
# from keras.preprocessing.sequence import pad_sequences
# from keras.models import Sequential
# from keras.layers import Dense, Embedding, LSTM
import json
from Configs.Config import Config
from Models.GoogleSearchResults import GoogleSearchResults
from Models.StockNews import StockNews
from Services.StockHistoryService import StockHistory
import bisect
from datetime import datetime, timedelta

class AIService:

    def __init__(self):
        print("AIService.Init")

    def BuildTestingModel(self, stockName):

        news = []
        with open(f'Reports/News/{stockName}-NewsReports.json') as f:
            data = json.load(f)
        stockNewsList = [GoogleSearchResults(**item) for item in data]
       
        stockNewsList.sort(key=lambda item : item.Date)
        stocksHistory = StockHistory().GetPriceHistoryByRange(stockName, stockNewsList[0].Date, stockNewsList[-1].Date)
        
        stockHistoryDates = set()
        for stockHistory in stocksHistory:
            stockHistoryDates.add(stockHistory.Dates)
        stockHistoryDatesList = list(stockHistoryDates)
        stockHistoryDatesList = sorted(stockHistoryDatesList, key=lambda date: datetime.strptime(date, "%Y-%m-%d"))

        distinctNewsDates = set()
        for news in stockNewsList:
            distinctNewsDates.add(news.Date)
        distinctNewsDatesList = list(distinctNewsDates)
        distinctNewsDatesList = sorted(distinctNewsDatesList, key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
        
        try:
            for date in distinctNewsDatesList:
                print(date)
                closestDateWorth = self.findClosestDate(date, stockHistoryDatesList)
                closestDateOneDay = self.findClosestDate(self.AddDaysToDate(date,1), stockHistoryDatesList)
                closestDateThreeDay = self.findClosestDate(self.AddDaysToDate(date,3), stockHistoryDatesList)
                closestDateOneWeek = self.findClosestDate(self.AddDaysToDate(date,5), stockHistoryDatesList)
                closestDateTwoWeek = self.findClosestDate(self.AddDaysToDate(date,10), stockHistoryDatesList)
                closestDateOneMonth = self.findClosestDate(self.AddDaysToDate(date,20), stockHistoryDatesList)

                stockHistoryDateWorth = self.findStockByDate(stocksHistory, closestDateWorth).Opens
                stockHistoryDateOneDay = (self.findStockByDate(stocksHistory, closestDateOneDay).Opens - stockHistoryDateWorth) / stockHistoryDateWorth
                stockHistoryDateThreeDay = (self.findStockByDate(stocksHistory, closestDateThreeDay).Opens - stockHistoryDateWorth) / stockHistoryDateWorth
                stockHistoryDateOneWeek = (self.findStockByDate(stocksHistory, closestDateOneWeek).Opens - stockHistoryDateWorth) / stockHistoryDateWorth
                stockHistoryDateTwoWeek = (self.findStockByDate(stocksHistory, closestDateTwoWeek).Opens - stockHistoryDateWorth) / stockHistoryDateWorth
                stockHistoryDateOneMonth = (self.findStockByDate(stocksHistory, closestDateOneMonth).Opens - stockHistoryDateWorth) / stockHistoryDateWorth
                stockNewsList = self.updateStockNews(stockNewsList, date, stockHistoryDateWorth, stockHistoryDateOneDay, stockHistoryDateThreeDay, stockHistoryDateOneWeek, stockHistoryDateTwoWeek, stockHistoryDateOneMonth)
        
        except Exception as e:
            print(str(e))
        return stockNewsList


    def updateStockNews(self, stockNewsList, targetDate, closestDateWorth, oneDayGain, threeDayGain, oneWeekGain, twoWeekGain, oneMonthGain):
        for stockNews in stockNewsList:
            if stockNews.Date == targetDate:
                stockNews.Worth = closestDateWorth
                stockNews.OneDayGain = oneDayGain
                stockNews.ThreeDayGain = threeDayGain
                stockNews.OneWeekGain = oneWeekGain,
                stockNews.TwoWeekGain = twoWeekGain,
                stockNews.OneMonthGain = oneMonthGain
        return stockNewsList

    def findStockByDate(self, stockHistoryList, targetDate):
        for stockHistory in stockHistoryList:
            if targetDate in stockHistory.Dates:
                return stockHistory
        
    def AddDaysToDate(self, dateString, days):
        dateFormat = "%Y-%m-%d"
        date = datetime.strptime(dateString, dateFormat)
        date += timedelta(days=days)
        return date.strftime(dateFormat)
    
    def findClosestDate(self, target, date_list):
        
        target = datetime.strptime(target, "%Y-%m-%d")
        date_list = [datetime.strptime(date, "%Y-%m-%d") for date in date_list]

        index = bisect.bisect_left(date_list, target)
        
        if index == 0:
            return date_list[0].strftime("%Y-%m-%d")
        if index == len(date_list):
            return date_list[-1].strftime("%Y-%m-%d")

        before = date_list[index - 1]
        after = date_list[index]

        if after - target < target - before:
            return after.strftime("%Y-%m-%d")
        else:
            return before.strftime("%Y-%m-%d")

        

    

    
        
    

    

    
    
