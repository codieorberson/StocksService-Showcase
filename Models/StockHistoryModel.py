
class StockHistoryModel:

    def __init__(self):
        self.Name = None
        self.Dates = None
        self.Opens = None
        self.Highs = None
        self.Lows = None
        self.Closes = None
        self.Volumes = None

    def SetFields(self, name, dates, opens, highs, lows, closes, volumes):
        self.Name = name
        self.Dates = dates
        self.Opens = opens
        self.Highs = highs
        self.Lows = lows
        self.Closes = closes
        self.Volumes = volumes
    

    
    
