from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class FeaturesForm(Form):
	feature = StringField('feature', validators = [DataRequired()])
	disclosureLocationA = StringField('disclosureLocationA')
	isDisclosedA = BooleanField('isDisclosedA')
	disclosureOpinionA = StringField('disclosureOpinionA')
