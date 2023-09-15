
from flask import jsonify
from flask_classful import FlaskView
from flask_restful import Resource, reqparse
from flask_classful import FlaskView, route
from Services.AuthService import AuthService

class AuthController(FlaskView):

    def __init__(self):
        print("AuthController.Init")
        self.authService = AuthService()

    @route('/Login', methods=['POST'])
    def Login(self):
        print("AuthController.Login")
        parser = reqparse.RequestParser()
        parser.add_argument("Username")
        parser.add_argument("Password")
        parser.add_argument("MfaCode")
        params = parser.parse_args()
        username = params["Username"]
        password = params["Password"]
        mfaCode = params["MfaCode"]
        status = self.authService.Login(username, password, mfaCode)
        
        response = {
            'response' : status
        }
        return jsonify(response)
    
    @route('/IsLoggedIn', methods=['GET'])
    def IsLoggedIn(self):
        print("AuthController.IsLoggedIn")
        status = self.authService.IsLoggedIn()
        response = {
            'response' : status
        }
        return jsonify(response)
    
    @route('/OneTimeLogin', methods=['POST'] )
    def OneTimeLogin(self):
        print("AuthController.Login")
        parser = reqparse.RequestParser()
        parser.add_argument("Username")
        parser.add_argument("Password")
        parser.add_argument("MfaCode")
        params = parser.parse_args()
        username = params["Username"]
        password = params["Password"]
        mfaCode = params["MfaCode"]
        status = self.authService.OneTimeLogin(username, password, mfaCode)
        response = {
            'response' : status
        }
        return jsonify(response)
    
    @route('/Logout', methods=['POST'] )
    def Logout(self):
        status = self.authService.Logout()
        response = {
            'response' : status
        }
        return jsonify(response)
   