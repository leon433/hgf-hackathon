from hgf_app import db


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
    noveltyScore = db.Column(db.Integer, index=True, unique=True)
    infringementScore = db.Column(db.Integer, index=True, unique=True)
    modOpinion = db.Column(db.Integer, index=True, unique=True)
    confidenceScore = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '< Feature: %s dLocA: %s isDisclosedA: %s disclosureOpinionA: %s >\n' % (self.feature, self.disclosureLocationA, self.isDisclosedA, self.disclosureOpinionA)

