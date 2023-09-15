class StockNews:

    def __init__(self, Name=None, Date=None, Title=None, Link=None, Worth=None, OneDayGain=None, ThreeDayGain=None, OneWeekGain=None):
        self.Name = Name
        self.Date = Date
        self.Title = Title
        self.Link = Link
        self.Worth = Worth
        self.OneDayGain = OneDayGain
        self.ThreeDayGain = ThreeDayGain
        self.OneWeekGain = OneWeekGain

    def __eq__(self, other):
        if isinstance(other, StockNews):
            return (self.Name, self.Date, self.Title, self.Link, self.Worth, self.OneDayGain, self.ThreeDayGain, self.OneWeekGain) == (other.Name, other.Date, other.Title, other.Link, other.Worth, other.OneDayGain, other.ThreeDayGain, other.OneWeekGain)
        return False

    def __hash__(self):
        return hash((self.Name, self.Date, self.Title, self.Link, self.Worth, self.OneDayGain, self.ThreeDayGain, self.OneWeekGain))
    
    def SetFields(self, name, date, title, link, worth=None, oneDayGain=None, threeDayGain=None, oneWeekGain=None):
        self.Name = name
        self.Date = date
        self.Title = title
        self.Link = link
        self.Worth = worth
        self.OneDayGain = oneDayGain
        self.ThreeDayGain = threeDayGain
        self.OneWeekGain = oneWeekGain