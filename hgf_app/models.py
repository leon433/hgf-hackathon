from hgf_app import db

#Database of features
class FeatureModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    feature = db.Column(db.String, index=True, unique=True) #Feature text

    # User A
    disclosureLocationA = db.Column(db.String, index=True, unique=True) #Location of nearest disclosure
    isDisclosedA = db.Column(db.Boolean, index=True, unique=True) #Is feature disclosed?
    disclosureOpinionA = db.Column(db.String, index=True, unique=True) #Why is feature disclosed?

    # User B
    disclosureLocationB = db.Column(db.String, index=True, unique=True)
    isDisclosedB = db.Column(db.Boolean, index=True, unique=True)
    disclosureOpinionB = db.Column(db.String, index=True, unique=True)

    # Moderators

    mod_score_ids = db.relationship('ModScoreModel', backref='feature', lazy='dynamic', primaryjoin="ModScoreModel.feature_id == FeatureModel.id")

    #noveltyScore = db.Column(db.Integer, index=True, unique=True)
    #infringementScore = db.Column(db.Integer, index=True, unique=True)
    #modOpinion = db.Column(db.Integer, index=True, unique=True)
    #confidenceScore = db.Column(db.Integer, index=True, unique=True)



    def __repr__(self):
        return '< ID: %s Feature: %s dLocA: %s isDisclosedA: %s disclosureOpinionA: %s >\n' % (self.id, self.feature, self.disclosureLocationA, self.isDisclosedA, self.disclosureOpinionA)


#Database of moderator scores
class ModScoreModel(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Unique score ID
    mod_id = db.Column(db.Integer, index=True) #ID of moderator 

    feature_id = db.Column(db.Integer, db.ForeignKey('feature_model.id')) #foreign key joining to Feature table
    

    noveltyScore = db.Column(db.Integer, index=True, unique=True)
    infringementScore = db.Column(db.Integer, index=True, unique=True)
    modOpinion = db.Column(db.Integer, index=True, unique=True)
    confidenceScore = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '< Score ID: %s Feature ID: %s noveltyScore %s >\n' % (self.id, self.feature_id, self.noveltyScore)

