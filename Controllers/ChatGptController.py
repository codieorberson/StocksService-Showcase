
from flask import jsonify
import openai
from flask_classful import FlaskView
from flask_restful import Resource, reqparse
from flask_classful import FlaskView, route
from Configs.Config import Config
from Helpers.JsonHelper import JsonHelper
from Services.ChatGptService import ChatGptService

class ChatGptController(FlaskView):

    def __init__(self):
        config = Config()
        self.apiKey = config.chatGptApiKey
        self.orgId = config.orgId
        self.chatGptService = ChatGptService(self.apiKey, self.orgId)
        self.jsonHelper = JsonHelper()

    @route('/GetAnswer', methods=['POST'] )
    def GetAnswer(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument("Question")
        params = parser.parse_args()
        question = params["Question"]
        answer = self.chatGptService.GetAnswer(question)
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/GetFineTuneAnswer', methods=['POST'] )
    def GetFineTuneAnswer(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Question")
        parser.add_argument("Id")
        params = parser.parse_args()
        question = params["Question"]
        id = params["Id"]
        answer = self.chatGptService.GetFineTuneAnswer(question, id)
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/CreatePicture', methods=['POST'] )
    def CreatePicture(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument("Prompt")
        parser.add_argument("Count")
        parser.add_argument("Size")
        params = parser.parse_args()
        prompt = params["Prompt"]
        count = int(params["Count"])
        size = params["Size"]
        answer = self.chatGptService.CreatePicture(prompt, count, size)
        response = {
            'message' : answer
        }
        return jsonify(response)

   
    @route('/CreateFineTune', methods=['POST'] )
    def CreateFineTune(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Id")
        parser.add_argument("Name")
        parser.add_argument("Gain")
        params = parser.parse_args()
        id = params["Id"]
        name = params["Name"]
        gain = params["Gain"]
        answer = self.chatGptService.CreateFineTune(id, name, gain)
        
        response = {
            'message' : answer
        }
        return jsonify(response)


    @route('/ListModels', methods=['POST'] )
    def ListModels(self):
        answer = self.chatGptService.ListModels()
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/GetModel', methods=['POST'] )
    def GetModel(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Id")
        params = parser.parse_args()
        id = params["Id"]
        answer = self.chatGptService.GetModel(id)
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/ListFiles', methods=['POST'] )
    def ListFiles(self):
        answer = self.chatGptService.ListFiles()
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/CreateJsonLFile', methods=['POST'] )
    def CreateJsonLFile(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        parser.add_argument("Gain")
        params = parser.parse_args()
        name = params["Name"]
        gain = params["Gain"]
        answer = self.jsonHelper.FineTuningConvertedJson(name, gain)
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/UploadFile', methods=['POST'] )
    def UploadFile(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        parser.add_argument("Gain")
        parser.add_argument("FileName")
        params = parser.parse_args()
        name = params["Name"]
        gain = params["Gain"]
        fileName = params["FileName"]
        answer = self.chatGptService.UploadFile(name, gain, fileName)

        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/ListFineTunes', methods=['POST'] )
    def ListFineTunes(self):
        answer = self.chatGptService.ListFineTunes()
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/GetFineTune', methods=['POST'] )
    def GetFineTune(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Id")
        params = parser.parse_args()
        id = params["Id"]
        answer = self.chatGptService.GetFineTune(id)
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/DeleteFineTune', methods=['POST'] )
    def DeleteFineTune(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Id")
        params = parser.parse_args()
        id = params["Id"]
        answer = self.chatGptService.DeleteFineTune(id)
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/CancelFineTune', methods=['POST'] )
    def CancelFineTune(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Id")
        params = parser.parse_args()
        id = params["Id"]
        answer = self.chatGptService.CancelFineTune(id)
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/DeleteFile', methods=['POST'] )
    def DeleteFile(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Id")
        params = parser.parse_args()
        id = params["Id"]
        answer = self.chatGptService.DeleteFile(id)
        response = {
            'message' : answer
        }
        return jsonify(response)
    
    @route('/DownloadFile', methods=['POST'] )
    def DownloadFile(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Id")
        params = parser.parse_args()
        id = params["Id"]
        answer = self.chatGptService.DownloadFile(id)
        response = {
            'message' : answer
        }
        return jsonify(response)
    

    @route('/RetrieveFile', methods=['POST'] )
    def RetrieveFile(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Id")
        params = parser.parse_args()
        id = params["Id"]
        answer = self.chatGptService.RetrieveFile(id)
        response = {
            'message' : answer
        }
        return jsonify(response)
    