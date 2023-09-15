
from datetime import datetime, timedelta
import requests
import robin_stocks.robinhood as rh
from pygooglenews import GoogleNews
import pandas as pd
from Configs.Config import Config
from Models.GoogleSearchResults import GoogleSearchResults
from Models.StockNews import StockNews
import time
import re
import requests
import urllib.parse
import json
import random
from scrapingbee import ScrapingBeeClient
from bs4 import BeautifulSoup

class News:

    def __init__(self):
        config = Config()
        self.stocksAbrDictionary = config.stocksDictionary
        self.scrapingBeeUrl = config.scrapingBeeUrl
        self.scrapingBeeApiKey = config.scrapingBeeApiKey

    def GetStories(self, name):
        return rh.stocks.get_news(name)
    
    def GetRatings(self, name):
        return rh.stocks.get_ratings(name)
    
    def RemoveSpecialCharacters(self, string):
        return re.sub('[^A-Za-z0-9 .!]', '', string)
    
    def GetStockNews(self, stockAbr, startDate, endDate):
        stockName = self.stocksAbrDictionary[stockAbr]
        searchResults = []
        startDate = datetime.strptime(startDate, '%Y-%m-%d')
        endDate = datetime.strptime(endDate, '%Y-%m-%d')
        currentDate = startDate
        length = 100
        days = 1
        count = 0
        errorCount = 0
        failureCount = 0
        randomNumber = random.randint(1, 1000000)
        client = ScrapingBeeClient(api_key=self.scrapingBeeApiKey)
        while currentDate <= endDate:

            if length < 20:
                days = 10
            elif length < 50:
                days = 4
            elif length < 75:
                days = 3
            else:
                days = 2

            count+=1
            if(count%10==0): 
                time.sleep(20)
                randomNumber = random.randint(1, 1000000)
            else: time.sleep(2)
            
            currentEndDate = currentDate + timedelta(days=days-1)

            searchParam = f'"{stockName}" after:{currentDate.strftime("%Y-%m-%d")} before:{currentEndDate.strftime("%Y-%m-%d")}'

            print(len(searchResults))
            print(currentDate.strftime("%Y-%m-%d") + " " + currentEndDate.strftime("%Y-%m-%d"))
            

            url = f'https://news.google.com/search?q={searchParam}'
            params = {
                'custom_google': 'True',
                'session_id': randomNumber,
                'json_response': 'True',
                'country_code': "us",
                "block_ads": 'True'
            }
            try:
                response = client.get(url=url,params=params)

                statusCode = response.status_code    
                if(statusCode != 200):
                    raise Exception(f"Error: Status Code {statusCode}")
                
                soup = BeautifulSoup(response.text, 'html.parser')
                h3_elements = soup.find_all('h3')
                for h3 in h3_elements:
                    a = h3.find('a')
                    div_sibling = h3.find_next_sibling('div')
                    if div_sibling:
                        time_element = div_sibling.find('div').find('time')
                        date = None
                        if time_element and 'datetime' in time_element.attrs:
                            date = time_element['datetime']
                            date = date.strip('Z').replace('\\"', '')[:10]
                        url = a['href']
                        description = ""
                        title = h3.text
                        reportDate = date
                        searchResult = GoogleSearchResults(stockAbr, url, description, title, reportDate)
                        searchResults.append(searchResult)
                length = len(h3_elements)
                currentDate += timedelta(days=days)
                failureCount = 0
                errorCount = 0
            except Exception as e:
                print(f"An error occured for {stockAbr}-{currentDate}: {str(e)}")
                print(f"Failure Count: {failureCount}")
                print(f"Error Count: {failureCount}")
                
                failureCount+=1
                errorCount+=1
                if failureCount >5:
                    return searchResults
                elif errorCount > 3:
                    time.sleep(60)
                    currentDate += timedelta(days=2)
                    continue
                else:
                    time.sleep(20)
                    continue
                
        return searchResults


    

    
    
