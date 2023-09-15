
import robin_stocks.robinhood as rh
import pyotp

from Configs.Config import Config

class AuthService:

    def __init__(self):
        print("AuthService.Init")

    # def Login(self, username, password, mfaCode):
    #     try:
    #         finalMfaCode = pyotp.TOTP(mfaCode).now()
    #         print(finalMfaCode)
    #         rh.authentication.login(username=username, password=password, mfa_code=finalMfaCode)
    #         return True
    #     except Exception as e:
    #         raise Exception(str(e))
        
    def Login(self, username, password, mfaCode):
        try:
            rh.authentication.login(username=username, password=password)
            return True
        except Exception as e:
            raise Exception(str(e))

    def OneTimeLogin(self, username, password, mfaCode):
        try:
            rh.authentication.login(username=username, password=password, mfa_code=mfaCode)
            return True
        except Exception as e:
            raise Exception(str(e))
        
    def IsLoggedIn(self):
        try:
            return True
            rh.authentication.login()
            return True
        except Exception:
            return False
    
    def Logout(self):
        try:
            rh.authentication.logout()
            return True
        except Exception as e:
            raise Exception(str(e))

    

    
        
    

    

    
    
