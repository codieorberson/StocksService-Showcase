
from flask_classful import FlaskView
from flask_classful import FlaskView, route

class HealthController(FlaskView):

    def __init__(self):
        print("HealthController.Init")

    @route('/HealthCheck')
    def HealthCheck(self):
        return 'OK'
   