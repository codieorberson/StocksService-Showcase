
import json
import pandas as pd
from Models.GoogleSearchResults import FullGoogleSearchResults

class JsonHelper:

    def FineTuningConvertedJson(self, stockName, gain):
        with open(f'Reports/News/{stockName}-FullNewsReports.json') as f:
            data = json.load(f)
        news = [FullGoogleSearchResults(**item) for item in data]
        convertedList = []
        for item in news:
            jsonItem = {"prompt": item.Title, "completion": self.formatFloat(getattr(item, gain))}
            convertedList.append(jsonItem)
        
        with open(f'Reports/News/{stockName}-{gain}-FineTunedReport.jsonl', 'w') as file:
            for item in convertedList:
                json.dump(item, file)
                file.write('\n')

        return True


    def GetSentimentLabel(self, value):
        if value < -0.15:
            return "Very Extremely Negative"
        elif -0.15 <= value < -0.10:
            return "Extremely Negative"
        elif -0.10 <= value < -0.05:
            return "Very Negative"
        elif -0.05 <= value < -0.025:
            return "Somewhat Negative"
        elif -0.025 <= value < 0:
            return "Slightly Negative"
        elif 0 <= value < 0.025:
            return "Slightly Positive"
        elif 0.025 <= value < 0.05:
            return "Somewhat Positive"
        elif 0.05 <= value < 0.10:
            return "Very Positive"
        elif 0.10 <= value < 0.15:
            return "Extremely Positive"
        else: # value >= 0.15
            return "Very Extremely Positive"
        
    def GetSentimentIntLabel(self, value):
        if value < -0.15:
            return 0
        elif -0.15 <= value < -0.10:
            return 1
        elif -0.10 <= value < -0.05:
            return 2
        elif -0.05 <= value < -0.025:
            return 3
        elif -0.025 <= value < 0:
            return 4
        elif 0 <= value < 0.025:
            return 5
        elif 0.025 <= value < 0.05:
            return 6
        elif 0.05 <= value < 0.10:
            return 7
        elif 0.10 <= value < 0.15:
            return 8
        else: # value >= 0.15
            return 9
        

    def formatFloat(self, val):
        formatted = "{:.4f}".format(val)
        number = formatted[1:] if formatted.startswith("0") else formatted
        finalNumber = self.getDecimalPart(number)
        return finalNumber
    
    def getDecimalPart(self, number):
        if(number[0]!= '-'): number= '+' + number
        operationSign = number[0]
        if number[0] in ['+', '-']:
            number = number[1:]

        if '.' in number:
            return operationSign + number.split('.')[1]
        else:
            return "0" 

        

    
    
