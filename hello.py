from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return Response('тут хуйня<br/>какаето')
@app.route('/data')
def data():
    diat = {"name : Igor ", "spacebar : __ ","amount : 24 "}
    return Response(diat)
if __name__ == '__main__':
    app.run()
