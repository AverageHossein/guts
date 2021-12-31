import os

class Base(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DB_USER = os.getenv('DATABASE_USERNAME')
    DB_PASS = os.getenv('DATABASE_PASSWORD')
    DB_HOST = os.getenv('DATABASE_URL')
    DB_PORT = os.getenv('DATABASE_PORT')
    DB_NAME = os.getenv('DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}' \
                              f'@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    