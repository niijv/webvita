# -*-coding: utf-8 -*-
#!flask/bin/python
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

from migrate.versioning import api

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
print 'Current database version: ' + str(api.db_version(
                    SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))