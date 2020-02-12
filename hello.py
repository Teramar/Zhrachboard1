from flask import Flask, Response, json
from flask.views import MethodView

app = Flask(__name__)


@app.route('/')
def hello_world() :
    return Response('тут хуйня<br/>какаето')


@app.route('/data')
def data() :
    diat = {'name' : 'Igor ', 'amount' : '24'}
    resp = Response(response=json.dumps(diat), status=200, mimetype="application/json")
    return resp


class CheckR(MethodView) :

    def get(self) :
        pmtd = ({"method" : "post"})
        if request.method == 'POST' :
            return Response(response=json.dumps(pmtd), status=200, mimetype="application/json")

    def post(self) :
        gmtd = {"method" : "get"}
        if request.method == 'GET' :
            return Response(response=json.dumps(gmtd), status=200, mimetype="application/json")

    methods = ['GET', 'POST']
    app.add_url_rule('/checker', view_func=checkr.as_view('checkr'))


if __name__ == '__main__' :
    app.run()
