
from flask import jsonify
from flask_classful import FlaskView
from flask_restful import Resource, reqparse
from flask_classful import FlaskView, route
from Models.GoogleSearchResults import FullGoogleSearchResults, GoogleSearchResults
from Services.AIService import AIService
import json
from datetime import datetime

class JsonController(FlaskView):

    @route('/RemoveTrailingSpace', methods=['POST'])
    def RemoveTrailingSpace(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        params = parser.parse_args()
        stockName= params["Name"]

        with open(f'Reports/News/{stockName}-NewsReports.json') as f:
            data = json.load(f)
        news = [GoogleSearchResults(**item) for item in data]

        serializedNews = [] 
        results = []
        for new in news:
            try:
                resultDate = new.Date.rstrip()
                resultDate = datetime.strptime(resultDate, '%b %d, %Y')
                resultDate = resultDate.strftime('%Y-%m-%d')
                result = GoogleSearchResults(stockName, new.Url, new.Description, new.Title, resultDate)
                results.append(result)
                print(new.Date)
            except Exception as e:
                print(f'Error: News For Loop: {str(e)}')
                continue

        for result in results:
            serializedItem = {
                "Name": result.Name,
                "Date": result.Date,
                "Title": result.Title,
                "Url": result.Url,
                "Description": result.Description
            }
            serializedNews.append(serializedItem)

        jsonData = json.dumps(serializedNews)
        filePath = f'Reports/News/{stockName}-NewsReportsReady.json'
        with open(filePath, 'w') as file:
            file.write(jsonData)
        return 'True'
      