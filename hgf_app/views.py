from hgf_app import app, db
from flask import render_template, redirect, request, jsonify
from .forms import FeaturesForm, FeaturesEditForm
from .models import FeatureModel, ModScoreModel


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/expert1')
def expert1():
    form = FeaturesForm()
    return render_template('expert1.html', form=form, title='Submit')


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
        separatedLocation = []
        if entry.disclosureLocationA is not None:
            separatedLocation = [x.strip() for x in entry.disclosureLocationA.split(',')]
        else:
            separatedLocation = [0, 0]

        if len(separatedLocation) < 2:
            separatedLocation = [0, 0]

        entryDict = {
            'id': entry.id,
            'feature': entry.feature,
            'disclosureLocation1': separatedLocation[0],
            'disclosureLocation2': separatedLocation[1] or separatedLocation[0],
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

####################################################################################################################

#USER 2

@app.route('/user2', methods=['GET', 'POST'])
def saveClaimFeature2():
    form = FeaturesForm()
    form2 = FeaturesEditForm()

    # if form.validate_on_submit():
    #     FormEntry = FeatureModel(feature=form.feature.data, disclosureLocationB=form.disclosureLocation.data,
    #                              isDisclosedA=form.isDisclosed.data, disclosureOpinionB=form.disclosureOpinion.data)
    #     db.session.add(FormEntry)
    #     db.session.commit()
    #     return redirect('/submitted')
    # print('FAIL')
    return render_template('user2.html', form=form, formEdit=form2, title='Submit')


@app.route('/user2/feature/submit')
def submitFeature2():
    feature = request.args.get('feature', "", type=str)
    disclosureLocationB = request.args.get('disclosureLocation', "", type=str)
    isDisclosedB = request.args.get('isDisclosed', type=bool)
    disclosureOpinionB = request.args.get('disclosureOpinion', type=str)

    FormEntry = FeatureModel(feature=feature, disclosureLocationB=disclosureLocationB,
                             isDisclosedB=isDisclosedB, disclosureOpinionB=disclosureOpinionB)
    db.session.add(FormEntry)
    db.session.commit()

    return jsonify({'status': 'OK'})


@app.route('/user2/feature/get')
def getFeature2():
    id = request.args.get('id', 0, type=int)
    feature = FeatureModel.query.get(id)

    return jsonify({
        'id': id,
        'feature': feature.feature,
        'disclosureLocation': feature.disclosureLocationA,
        'isDisclosed': feature.isDisclosedB,
        'disclosureOpinion': feature.disclosureOpinionB
    })


@app.route('/user2/features/get')
def getFeatures2():
    # need to filter by patentee
    entries = FeatureModel.query.all()
    entriesList = []
    for entry in entries:
        separatedLocation = []
        if entry.disclosureLocationB is not None:
            separatedLocation = [x.strip() for x in entry.disclosureLocationB.split(',')]
        else:
            entry.disclosureLocationB = entry.disclosureLocationA

        if entry.disclosureLocationB is None:
            separatedLocation = [0, 0]

        if len(separatedLocation) < 2:
            separatedLocation = [0, 0]

        entryDict = {
            'id': entry.id,
            'feature': entry.feature,
            'disclosureLocation1': separatedLocation[0],
            'disclosureLocation2': separatedLocation[1],
            'isDisclosed': entry.isDisclosedB,
            'disclosureOpinion': entry.disclosureOpinionB}
        entriesList.append(entryDict)

    return jsonify(entriesList)


@app.route('/user2/feature/edit')
def editFeature2():
    id = request.args.get('id', 0, type=int)
    record = FeatureModel.query.get(id)

    feature = request.args.get('feature', "", type=str)
    disclosureLocation = request.args.get('disclosureLocation', "", type=str)
    isDisclosed = request.args.get('isDisclosed', type=bool)
    disclosureOpinion = request.args.get('disclosureOpinion', type=str)

    record.feature = feature
    record.disclosureLocationB = disclosureLocation
    record.isDisclosedB = isDisclosed
    record.disclosureOpinionB = disclosureOpinion
    db.session.commit()
    return jsonify({'status': 'OK'})


@app.route('/user2/feature/delete')
def deleteFeature2():
    id = request.args.get('id', 0, type)
    db.session.delete(id)
    db.session.commit()
    return jsonify({'status': 'OK'})


@app.route('/expert1/features/get')
def getFeaturesForExperts():
    # need to filter by patentee
    entries = FeatureModel.query.all()
    entriesList = []
    for entry in entries:
        separatedLocation = []
        if entry.disclosureLocationA is not None:
            separatedLocation = [x.strip() for x in entry.disclosureLocationA.split(',')]
        else:
            separatedLocation = [0, 0]

        if len(separatedLocation) < 2:
            separatedLocation = [0, 0]

        entryDict = {
            'id': entry.id,
            'feature': entry.feature,
            'disclosureLocation1': separatedLocation[0],
            'disclosureLocation2': separatedLocation[1] or separatedLocation[0],
            'isDisclosedA': entry.isDisclosedA,
            'isDisclosedB': entry.isDisclosedB,
            'disclosureOpinionA': entry.disclosureOpinionA,
            'disclosureOpinionB': entry.disclosureOpinionB}
        entriesList.append(entryDict)

    return jsonify(entriesList)

@app.route('/expert1/score/post')
def submitScores():
    modId = request.args.get('modId', "", type=int)
    featureIds = request.args.get('featureId', "", type=str)
    noveltyScore = request.args.get('noveltyScore', "", type=str)
    infringementScore = request.args.get('infringementScore', "", type=str)
    expertOpinion = request.args.get('expertOpinion', "", type=str)

    FormEntry = ModScoreModel(modId=modId, featureIds=featureIds, noveltyScore=noveltyScore,
                              infringementScore=infringementScore, expertOpinion=expertOpinion);
    db.session.add(FormEntry)
    db.session.commit()
