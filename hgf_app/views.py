from hgf_app import app, db
from flask import render_template, redirect, request, jsonify
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


@app.route('/patentee1/feature/submit')
def submitFeature():
    feature = request.args.get('feature', "", type=str)
    disclosureLocationA = request.args.get('disclosureLocation', "", type=str)
    isDisclosedA = request.args.get('isDisclosed', type=bool)
    disclosureOpinionA = request.args.get('disclosureOpinion', type=str)

    FormEntry = FeatureModel(feature=feature, disclosureLocationA=disclosureLocationA,
                             isDisclosedA=isDisclosedA, disclosureOpinionA=disclosureOpinionA)
    db.session.add(FormEntry)
    db.session.commit()

    return jsonify({'status': 'OK'})


@app.route('/patentee1/feature/get')
def getFeature():
    id = request.args.get('id', 0, type=int)
    feature = FeatureModel.query.get(id)

    return jsonify({
        'feature': feature.feature,
        'disclosureLocation': feature.disclosureLocationA,
        'isDisclosed': feature.isDisclosedA,
        'disclosureOpinion': feature.disclosureOpinionA
    })


@app.route('/patentee1/features/get')
def getFeatures():
    # need to filter by patentee
    entries = FeatureModel.query.all()
    entriesList = []
    for entry in entries:
        separatedLocation =[]
        if entry.disclosureLocationA is not None:
            separatedLocation = [x.strip() for x in entry.disclosureLocationA.split(',')]
        else:
            separatedLocation = [0, 0]

        entryDict = {
            'id': entry.id,
            'feature': entry.feature,
            'disclosureLocation1': separatedLocation[0],
            'disclosureLocation2': separatedLocation[1],
            'isDisclosed': entry.isDisclosedA,
            'disclosureOpinion': entry.disclosureOpinionA}
        entriesList.append(entryDict)

    return jsonify(entriesList)


@app.route('/patentee1/feature/delete')
def deleteFeature():
    id = request.args.get('id', 0, type=int)
    feature = FeatureModel.query.get(id)
    db.session.delete(feature)
    db.session.commit()
    return jsonify({'status': 'OK'})


@app.route('/submitted')
def submitted():
    return render_template('submitted.html')
