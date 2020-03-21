import flask
from flask import json
from flask.views import MethodView


def hello_world() :
    return flask.Response('тут хуйня<br/>какаето')


def data():
    diat = {'name' : 'Igor ', 'amount' : '24'}
    resp = flask.Response(response=json.dumps(diat), status=200, mimetype="application/json")
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
class comp_arr(MethodView):
    def get(self)  :
        lst = [1, 2, 3, 4, 7, 10, 14, 22, 23, 24]
        result = []
        tmp = []
        for i, v in enumerate(lst) :
            if tmp :
                if v == tmp[-1] + 1 :
                    tmp.append(v)

                else :
                    if len(tmp) == 1 :
                        result.append(tmp[0])

                    else :
                        result.append(f'{tmp[0]}-{tmp[-1]}')

                    tmp = [v]
            else :
                tmp.append(v)

            if i == len(lst) - 1 :
                if len(tmp) == 1 :
                    result.append(tmp[0])

                else :
                    result.append(f'{tmp[0]}-{tmp[-1]}')
                    print(', '.join(map(str, result)))
        return {
            "request" : [1, 2, 3, 4, 7, 10, 14, 22, 23, 24],
            "compressed" : &&&&
            }