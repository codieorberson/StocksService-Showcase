from datetime import datetime, timedelta
from Models.StockNews import StockNews
from Services.NewsService import News
from flask_restful import reqparse
from flask_classful import FlaskView, route
import json
import robin_stocks.robinhood as rh
from flask import jsonify
import datetime
import re
class NewsController(FlaskView):

    def __init__(self):
        self.news = News()

    def GetStories(self, name):
        news = self.news.GetStories(name)
        return json.dumps(news)
    
    def GetRatings(self, name):
        ratings = self.news.GetRatings(name)
        return json.dumps(ratings)
    
    @route('/GetStockNews', methods=['POST'] )
    def GetStockNews(self):
        startTime = datetime.datetime.now()
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        parser.add_argument("StartDate")
        parser.add_argument("EndDate")
        params = parser.parse_args()
        names= params["Name"].split(",")
        startDate= params["StartDate"]
        endDate= params["EndDate"]
        for name in names:
        
            stockNewsList = self.news.GetStockNews(name, startDate, endDate)
            serializedNews = []
            for item in stockNewsList:
                serializedItem = {
                    "Name": item.Name,
                    "Date": self.removeSpecialCharacters(item.Date),
                    "Title": self.removeSpecialCharacters(item.Title),
                    "Url": self.removeSpecialCharacters(item.Url),
                    "Description": item.Description
                }
                serializedNews.append(serializedItem)

            jsonData = json.dumps(serializedNews)
            filePath = f'Reports/News/{name}-NewsReports.json'
            with open(filePath, 'w') as file:
                file.write(jsonData)
            
            
            print(f'Took this long to run: {datetime.datetime.now() - startTime}')

        return jsonData
    
    def removeSpecialCharacters(self, string):
        pattern = r'[^\x00-\x7F]'
        cleaned_string = re.sub(pattern, '', string)
        return cleaned_string
