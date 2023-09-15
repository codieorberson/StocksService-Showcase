from flask import jsonify
from flask_restful import reqparse
from flask_classful import FlaskView, route
from Services.StockHistoryService import StockHistory
import json

class StockInfoController(FlaskView):

    @route('/GetStocksPriceHistory', methods=['POST'] )
    def GetStocksPriceHistory(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Stocks")
        parser.add_argument("Period")
        parser.add_argument("Interval")
        params = parser.parse_args()
        names= params["Stocks"].split(",")
        period= params["Period"]
        interval= params["Interval"]
        history = StockHistory().GetStocksPriceHistory(names, period, interval)
        serialized_history = []
        for item in history:
            serialized_item = {
                "Name": item.Name,
                "Dates": item.Dates,
                "Opens": item.Opens,
                "Highs": item.Highs,
                "Lows": item.Lows,
                "Closes": item.Closes,
                "Volumes": item.Volumes
            }
            serialized_history.append(serialized_item)
        return jsonify(serialized_history)
    