from flask.views import MethodView

class Check_R(MethodView) :
    @property
    def get(self) :
        return {
            'method' : 'get'
        }

    def post(self) :
        return {
            'method' : 'post'
        }