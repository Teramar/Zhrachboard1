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


class Check_R(MethodView) :
    def get(self) :
        return {
            'method' : 'get'
        }

    def post(self) :
        return {
            'method' : 'post'
        }


app.add_url_rule('/checkapproute', view_func=Check_R.as_view('checkr'), methods=['GET', 'POST'])
if __name__ == '__main__' :
    app.run()
