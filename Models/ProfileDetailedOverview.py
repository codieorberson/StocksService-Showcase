class ProfileDetailedOverview:

    def __init__(self):
        self.Name = None
        self.InitialWorth = None
        self.CurrentWorth = None
        self.GainPrice = None
        self.GainPercentage = None
        self.InstrumentId = None
        self.InitialSharePrice = None
        self.CurrentSharePrice = None

    def SetFields(self, name, initialWorth, currentWorth, gainPrice, gainPercentage, instrumentId, initialSharePrice, currentSharePrice):
        self.Name = name
        
        self.InitialWorth = round(initialWorth,2)
        print(self.InitialWorth)
        self.CurrentWorth = round(currentWorth, 2)
        self.GainPrice = round(gainPrice, 2)
        self.GainPercentage = round(gainPercentage, 3)
        self.InstrumentId = instrumentId
        self.InitialSharePrice = round(initialSharePrice, 2)
        self.CurrentSharePrice = round(currentSharePrice, 2)
