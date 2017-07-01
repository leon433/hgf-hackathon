from hgf_app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/patentee1')
def patentee1():
    return render_template('patentee1.html')

