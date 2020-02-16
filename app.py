from views import flask, Check_R, data, hello_world

app = flask.Flask(__name__)
app.add_url_rule('/checkapproute', 'checkr', Check_R, methods=['GET', 'POST'])
app.add_url_rule('/data', 'data', data, methods=['GET', 'POST'])
app.add_url_rule('/', 'hello_world', hello_world, methods=['GET', 'POST'])
if __name__ == '__main__' :
    app.run()
