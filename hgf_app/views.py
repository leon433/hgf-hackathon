from hgf_app import app

@app.route('/')
@app.route('/index')
def index():
	return 'testing'