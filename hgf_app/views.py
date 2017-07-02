from hgf_app import app, db
from flask import render_template, flash, redirect
from .forms import FeaturesForm
from .models import FeatureModel


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/patentee1', methods=['GET', 'POST'])
def saveClaimFeature():
    form = FeaturesForm()

    if form.validate_on_submit():
        FormEntry = FeatureModel(feature=form.feature.data, disclosureLocationA=form.disclosureLocation.data,
                                 isDisclosedA=form.isDisclosed.data, disclosureOpinionA=form.disclosureOpinion.data)
        db.session.add(FormEntry)
        db.session.commit()
        return redirect('/submitted')
    print('FAIL')
    return render_template('patentee1.html', form=form, title='Submit')


@app.route('/submitted')
def submitted():
    return render_template('submitted.html')
