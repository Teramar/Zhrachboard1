from views import flask, Check_R, Data, Hello_world, Comp_arr

app = flask.Flask(__name__)
app.add_url_rule('/checkapproute',  view_func=Check_R.as_view('checkr'), methods=['GET', 'POST'])
app.add_url_rule('/data', 'data',  view_func=Data,  methods=['GET', 'POST'])
app.add_url_rule('/', 'hello_world', Hello_world, methods=['GET', 'POST'])
app.add_url_rule('/compress', view_func=Comp_arr.as_view('comparr'), methods=['GET'])
if __name__ == '__main__' :
    app.run()
