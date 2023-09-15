class Config:
     def __init__(self):
          self.frontendUrls = ["http://localhost:4200"]
          self.chatGptApiKey = ""
          self.orgId = ""
          self.stocksDictionary = {
               "CRM": "Salesforce",
               "GOOG": "Google",
               "MSFT": "Microsoft",
               "ELV": "Elevance Health",
               "UNH" : "UnitedHealth Group",
               "CI": "Cigna",
               "DIS": "Disney",
               "PGR": "Progressive Insurance",
               "PEP": "Pepsi",
               "AMZN": "Amazon",
               "XOM": "Exxon Mobil",
               "TSLA": "Tesla",
               "BUD": "Anheuser-Busch InBev"
          }
          self.scrapingBeeUrl = ''
          self.scrapingBeeApiKey = ''