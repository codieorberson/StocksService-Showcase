from flask_restful import Resource, reqparse
from Services.StockHistoryService import StockHistory
from Services.StocksAnalysesService import StocksAnalyses
from Helpers.CsvHelper import CsvHelper
from flask_classful import FlaskView

class CsvController(FlaskView):

    def BuildOverview(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Stocks")
        params = parser.parse_args()
        stockNames= params["Stocks"].split(",")
        stockAnalysis = StocksAnalyses(stockNames)
        csvHelper = CsvHelper(stockNames)
        csvHelper.CreateGainLossCsv(stockAnalysis)
        return "true"
    
    def BuildStockPerformance(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Stocks")
        parser.add_argument("Span")
        parser.add_argument("Interval")
        params = parser.parse_args()
        names= params["Stocks"].split(",")
        span= params["Span"]
        interval= params["Interval"]

        csvHelper = CsvHelper(names)
        for name in names:
            stockHistory = StockHistory(name, interval=interval, span=span).history
            csvHelper.CreateStockReportCsv(name, stockHistory, span, interval)

        return "true"
   