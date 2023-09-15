from Controllers.AIController import AIController
from Controllers.AuthController import AuthController
from Controllers.CsvController import CsvController
from Controllers.JsonController import JsonController
from Controllers.NewsController import NewsController
from Controllers.PortfolioController import PortfolioController
from Controllers.ChatGptController import ChatGptController
from Controllers.HealthController import HealthController
from flask import Flask, jsonify
from flask_cors import CORS
from Configs.Config import Config
import sys
from Controllers.StockInfoController import StockInfoController

print("Starting Project")
app = Flask(__name__)
app.config['TIMEOUT'] = 3600
config = Config()
# cors = CORS(app, resources={r"/*": {"origins": config.frontendUrls}})
cors = CORS(app, resources={r"/*": {"origins": "*"}})

HealthController.register(app, route_base='/api/v1/Health')
AuthController.register(app, route_base='/api/v1/Auth')
StockInfoController.register(app, route_base='/api/v1/StockInfo')
NewsController.register(app, route_base='/api/v1/News')
PortfolioController.register(app, route_base='/api/v1/Portfolio')
CsvController.register(app, route_base='/api/v1/Csv')
ChatGptController.register(app, route_base='/api/v1/ChatGpt')
AIController.register(app, route_base='/api/v1/AI')
JsonController.register(app, route_base='/api/v1/Json')

print("Completing Setup Project")
if __name__ == '__main__':      
   app.run(debug=True)


