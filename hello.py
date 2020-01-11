from flask import Flask, Response, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return Response('тут хуйня<br/>какаето')
@app.route('/data')
def data():
    name = 'Igor'
    amount = '24'
    return jsonify(name, amount)
if __name__ == '__main__':
    app.run()
