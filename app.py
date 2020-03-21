from views import flask, Check_R, data, hello_world, comp_arr

app = flask.Flask(__name__)
app.add_url_rule('/checkapproute', endpoint=None, view_func=Check_R.as_view('checkr'), methods=['GET', 'POST'])
app.add_url_rule('/data', 'data',  view_func=data,  methods=['GET', 'POST'])
app.add_url_rule('/', 'hello_world', hello_world, methods=['GET', 'POST'])
app.add_url_rule('/compress?arr', endpoint=None, view_func=comp_arr.as_view('comparr'), methods=['GET'])
if __name__ == '__main__' :
    app.run()
