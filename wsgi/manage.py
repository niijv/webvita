# -*-coding: utf-8 -*-
#!flask/bin/python
from webvita import app, db

from config import SQLALCHEMY_MIGRATE_REPO

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

migrate = Migrate(app, db, directory=SQLALCHEMY_MIGRATE_REPO)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
