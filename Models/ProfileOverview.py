
class ProfileOverview:

    def __init__(self):
        self.GainLoss = None
        self.GainLossPercent = None
        self.Invested = None
        self.Worth = None

    def SetFields(self, gainLoss, gainLossPercent, invested, worth):
        self.GainLoss = round(gainLoss, 2)
        self.GainLossPercent = round(gainLossPercent, 2)
        self.Invested = round(invested, 2)
        self.Worth = round(worth, 2)
    

    
    
