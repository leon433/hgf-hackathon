from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class FeaturesForm(Form):
    feature = StringField('feature', validators=[DataRequired()])
    disclosureLocation = StringField('disclosureLocation')
    isDisclosed = BooleanField('isDisclosed')
    disclosureOpinion = StringField('disclosureOpinion')


class FeaturesEditForm(Form):
    editFeature = StringField('editFeature', validators=[DataRequired()])
    disclosureEditLocation = StringField('disclosureEditLocation')
    isEditDisclosed = BooleanField('isEditDisclosed')
    disclosureEditOpinion = StringField('disclosureEditOpinion')