from hgf_app import app, db
from flask import render_template, flash, redirect
from .forms import FeaturesForm
from .models import FeatureModel


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/patentee1', methods = ['GET', 'POST'])
def saveClaimFeature():
	form = FeaturesForm()

	FormEntry = FeatureModel(feature=form.feature.data, disclosureLocationA=form.disclosureLocationA.data, isDisclosedA=form.isDisclosedA.data, disclosureOpinionA=form.disclosureOpinionA.data)
	db.session.add(FormEntry)
	db.session.commit()
	return render_template('patentee1.html', form=form, title='Submit')

