import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'stumble.db')
SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/swigraph'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
