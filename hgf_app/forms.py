from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class FeaturesForm(Form):
	feature1 = StringField('feature1', validators = [DataRequired()])
	feature2 = StringField('feature2', validators = [DataRequired()])
	feature3 = StringField('feature3', validators = [DataRequired()])