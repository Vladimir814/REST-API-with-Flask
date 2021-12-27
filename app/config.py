import psycopg2
from decouple import config


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
    conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI, sslmode='require')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
