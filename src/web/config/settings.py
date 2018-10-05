import os

basedir = os.path.abspath(os.path.dirname(__file__))


class GoogleAuth:
    CLIENT_ID = ('688061596571-3c13n0uho6qe34hjqj2apincmqk86ddj'
                 '.apps.googleusercontent.com')
    CLIENT_SECRET = 'JXf7Ic_jfCam1S7lBJalDyPZ'
    REDIRECT_URI = 'https://localhost:5000/gCallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = [
                "https://www.googleapis.com/auth/plus.me",
                "https://www.googleapis.com/auth/userinfo.email",
            ]


class Dev:
    APP_NAME = "itemcatalog"
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "development"
    ENV = os.environ.get("ENV") or 'development'
    SERVER = os.environ.get("SERVER") or 'localhost'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///egu-nyc-dev-001.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Test(Dev):
    DEBUG = False
    TESTING = True
    ENV = os.environ.get("ENV") or 'test'
    SERVER = os.environ.get("SERVER") or "egu-nyc-dev-001"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///egu-nyc-test-001.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Prod(Test):
    DEBUG = False
    TESTING = False
    ENV = os.environ.get("ENV") or 'production'
    SERVER = os.environ.get("SERVER") or "egu-nyc-prd-001"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///egu-nyc-prd-001.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
