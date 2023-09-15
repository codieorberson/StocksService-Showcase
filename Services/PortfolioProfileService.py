
import robin_stocks.robinhood as rh
class PortfolioProfile:

    def GetCurrentEquity(self):
        return self.GetPortfolio()["equity"]

    def GetPortfolio(self):
        return rh.profiles.load_portfolio_profile()

    def GetEquityPreviousClose(self):
        return self.GetPortfolio()["equity_previous_close"]


    
    
