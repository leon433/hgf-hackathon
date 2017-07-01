from hgf_app import db


class ClaimsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    features = db.Column(db.String, index=True, unique=True)

    # User A
    disclosureLocationA = db.Column(db.String, index=True, unique=True)
    isDisclosedA = db.Column(db.Boolean, index=True, unique=True)
    disclosureOpinionA = db.Column(db.String, index=True, unique=True)

    # User B
    disclosureLocationB = db.Column(db.String, index=True, unique=True)
    isDisclosedB = db.Column(db.Boolean, index=True, unique=True)
    disclosureOpinionB = db.Column(db.String, index=True, unique=True)

    # Moderators
    noveltyScore = db.Column(db.Integer, index=True, unique=True)
    inventiveScore = db.Column(db.Integer, index=True, unique=True)
    infringementScore = db.Column(db.Integer, index=True, unique=True)
    modOpinion = db.Column(db.Integer, index=True, unique=True)
    confidenceScore = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % self.features
