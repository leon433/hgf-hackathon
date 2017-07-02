#!flask/bin/python
from hgf_app import db, models
models.ModScoreModel.query.all()