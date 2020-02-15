import flask
from flask.views import MethodView


@app.route('/')
def hello_world() :
    return flask.Response('тут хуйня<br/>какаето')
@app.route('/data')
def data() :
    diat = {'name' : 'Igor ', 'amount' : '24'}
    resp = flask.Response(response=flask.json.dumps(diat), status=200, mimetype="application/json")
    return resp


class Check_R(MethodView) :
    def get(self) :
        return {
            'method' : 'get'
        }

    def post(self) :
        return {
            'method' : 'post'
        }