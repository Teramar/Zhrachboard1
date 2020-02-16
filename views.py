import flask
from flask import json
from flask.views import MethodView


def hello_world() :
    return flask.Response('тут хуйня<br/>какаето')


def data() :
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
