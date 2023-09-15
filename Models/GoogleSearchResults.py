
class GoogleSearchResults:
    def __init__(self, Name, Url, Description, Title, Date):
        self.Name = Name
        self.Url = Url
        self.Description = Description
        self.Title = Title
        self.Date = Date
        self.Worth = None
        self.OneDayGain = None
        self.ThreeDayGain = None
        self.OneWeekGain = None
        self.TwoWeekGain = None
        self.OneMonthGain = None

class FullGoogleSearchResults:
    def __init__(self, Name, Url, Description, Title, Date, Worth, OneDayGain, ThreeDayGain, OneWeekGain, TwoWeekGain, OneMonthGain):
        self.Name = Name
        self.Url = Url
        self.Description = Description
        self.Title = Title
        self.Date = Date
        self.Worth = Worth
        self.OneDayGain = OneDayGain
        self.ThreeDayGain = ThreeDayGain
        self.OneWeekGain = OneWeekGain
        self.TwoWeekGain = TwoWeekGain
        self.OneMonthGain = OneMonthGain

    
    
