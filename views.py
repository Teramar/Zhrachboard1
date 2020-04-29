import flask
from flask import json, request
from flask.views import MethodView


def Hello_world() :
    return flask.Response('тут хуйня<br/>какаето')


def Data() :
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


class Comp_arr(MethodView) :
    def get(self) :
        # lst = [1,2,3,4,7,10,14,22,23,24]
        lst = request.args.getlist('arr')
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
                    # print(', '.join(map(str, result)))
                arrz = {'array' : lst, 'compressed array' : ', '.join(result)}
                responz = flask.Response(response=json.dumps(arrz), status=200, mimetype="application/json")
                return responz
