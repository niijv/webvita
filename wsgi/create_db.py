# -*-coding: utf-8 -*-
#!flask/bin/python

from webvita import db, models
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

from migrate.versioning import api

import os.path

from passlib.apps import custom_app_context as pwd_context

def db_setup_dev(name, realname, pw, email):
    db.drop_all()
    db.create_all()
    admin = models.User(name, realname, pwd_context.encrypt(pw), email)
    db.session.add(admin)
    db.session.commit()
    
def db_reset():
    db.drop_all()
    db.create_all()
    
def init_db_migrate():
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI, 
                            SQLALCHEMY_MIGRATE_REPO, 
                            api.version(SQLALCHEMY_MIGRATE_REPO))
                           
#db_setup_dev('dummy', 'Mr. Dummy', 'dummy', 'dummy@mail.com')
db_reset()
init_db_migrate()
