from flask_restful import reqparse
from Services.StocksAnalysesService import StocksAnalyses
from flask_classful import FlaskView, route


class PortfolioController(FlaskView):

    @route('/GetOverview', methods=['POST'] )
    def GetOverview(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Stocks")
        params = parser.parse_args()
        stockNames= params["Stocks"].split(",")
        stockAnalysis = StocksAnalyses(stockNames)
        return stockAnalysis.GetOverview()
    
    @route('/GetDetailedOverview', methods=['POST'])
    def GetDetailedOverview(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Stocks")
        params = parser.parse_args()
        stockNames= params["Stocks"].split(",")
        stockAnalysis = StocksAnalyses(stockNames)
        return stockAnalysis.GetDetailedOverview()