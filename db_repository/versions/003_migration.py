from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
claims_model = Table('claims_model', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('features', VARCHAR),
    Column('disclosureLocationA', VARCHAR),
    Column('isDisclosedA', BOOLEAN),
    Column('disclosureOpinionA', VARCHAR),
    Column('disclosureLocationB', VARCHAR),
    Column('isDisclosedB', BOOLEAN),
    Column('disclosureOpinionB', VARCHAR),
    Column('noveltyScore', INTEGER),
    Column('inventiveScore', INTEGER),
    Column('infringementScore', INTEGER),
    Column('modOpinion', INTEGER),
    Column('confidenceScore', INTEGER),
)

feature_model = Table('feature_model', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('feature', String),
    Column('disclosureLocationA', String),
    Column('isDisclosedA', Boolean),
    Column('disclosureOpinionA', String),
    Column('disclosureLocationB', String),
    Column('isDisclosedB', Boolean),
    Column('disclosureOpinionB', String),
    Column('noveltyScore', Integer),
    Column('infringementScore', Integer),
    Column('modOpinion', Integer),
    Column('confidenceScore', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['claims_model'].drop()
    post_meta.tables['feature_model'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['claims_model'].create()
    post_meta.tables['feature_model'].drop()
