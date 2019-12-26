from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return Response('тут хуйня<br/>какаето')

if __name__ == '__main__':
    app.run()
