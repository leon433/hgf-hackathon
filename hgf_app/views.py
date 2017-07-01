from hgf_app import app
from flask import render_template, flash, redirect
from .forms import FeaturesForm


@app.route('/')
@app.route('/index')
def index():

	return render_template('index.html')

@app.route('/patentee1', methods = ['GET', 'POST'])
def patentee1():
	form = FeaturesForm()

	return render_template('patentee1.html', form=form, title='Submit')