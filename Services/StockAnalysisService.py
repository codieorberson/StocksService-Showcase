import json
from Models.ProfileDetailedOverview import ProfileDetailedOverview
import robin_stocks.robinhood as rh
class StockAnalysis:

    def __init__(self, name):
        self.name = name
        self.SetInstrumentId()
        self.SetCurrentStockPrice()
        self.SetBoughtStockPrice()
        self.SetCurrentStockWorth()
        self.SetBoughtStockWorth()
        self.SetPositiveStatus()
        self.SetGainLossPercent()
        self.SetGainLossPrice()

    def __call__(self):
        detailedOverview = ProfileDetailedOverview()
        detailedOverview.SetFields(self.name, self.boughtStockWorth, self.currentStockWorth, self.gainLossPrice, self.gainLossPercent, self.id, self.boughtStockPrice, self.currentStockPrice)
        return json.dumps(detailedOverview.__dict__)

    def SetInstrumentId(self):
        self.id = rh.stocks.get_instruments_by_symbols(self.name)[0]['id']

    def SetCurrentStockPrice(self):
        self.currentStockPrice = float(rh.stocks.get_latest_price(self.name)[0])

    def SetBoughtStockPrice(self):
        positions = rh.account.get_all_positions()
        for position in positions:
            if(position["instrument_id"] == self.id):
                self.boughtStockPrice = float(position["average_buy_price"])
                self.quantity = float(position["quantity"])
    
    def SetCurrentStockWorth(self):
        self.currentStockWorth = float(self.currentStockPrice) * float(self.quantity)

    def SetBoughtStockWorth(self):
        self.boughtStockWorth = float(self.boughtStockPrice) * float(self.quantity)

    def SetPositiveStatus(self):
        if(self.boughtStockPrice >= self.currentStockPrice):
            self.positiveStatus = False
        else:
            self.positiveStatus = True

    def SetGainLossPercent(self):
        if(self.positiveStatus):
            self.gainLossPercent = (float(self.currentStockPrice) - float(self.boughtStockPrice)) / float(self.currentStockPrice)
        else:
            self.gainLossPercent = -abs((float(self.boughtStockPrice) - float(self.currentStockPrice)) / float(self.boughtStockPrice))
        
    def SetGainLossPrice(self):
        if(self.positiveStatus):
            self.gainLossPrice = float(self.currentStockWorth) - float(self.boughtStockWorth)
        else:
            self.gainLossPrice = -abs(float(self.boughtStockWorth) - float(self.currentStockWorth))

   

    
    
