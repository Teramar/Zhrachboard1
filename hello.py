from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return Response('тут хуйня<br/>какаето')
@app.route('/data')
def data():
    diat = {'name' : 'Igor', 'spacebar':' ','amount' : '24'}
    resp = Response(response = diat.values(),
                    status = 200,
                    mimetype = "application/json")
    return resp
if __name__ == '__main__':
    app.run()
