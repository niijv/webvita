# -*-coding: utf-8 -*-
#!flask/bin/python
import os

SECRET_KEY = "very secret"
DEBUG = True
SQLALCHEMY_ECHO = False

if os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL'):
    SQLALCHEMY_DATABASE_URI = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
else:
    SQLALCHEMY_DATABASE_URI = \
            'postgresql://postgres:postgres@localhost/webvita-local'

if os.environ.get('OPENSHIFT_DATA_DIR'):
    SQLALCHEMY_MIGRATE_REPO = os.path.join(os.environ['OPENSHIFT_DATA_DIR'],
                                           'db/migration_repo/')
else:
    SQLALCHEMY_MIGRATE_REPO = os.path.join(os.path.dirname(__file__), 
                                           'db_local/migration_repo/')

#Openshift: 'OPENSHIFT_POSTGRESQL_DB_URL'
#Heroku: 'DATABASE_URL'

