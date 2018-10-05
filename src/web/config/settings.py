import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Dev:
    APP_NAME = "itemcatalog"
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "development"
    ENV = os.environ.get("ENV") or 'development'
    SERVER = os.environ.get("SERVER") or 'localhost'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///egu-nyc-dev-001.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_OAUTH_CLIENT_ID = ('718620819024-p79474kp950rtb6kobs8r6622akb6j62'
                              '.apps.googleusercontent.com')
    GOOGLE_OAUTH_CLIENT_SECRET = 'E2KqzJFHFRoPTm81Zwe5ifW7'
    GOOGLE_OAUTH_CLIENT_SCOPE = [
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ]
    GOOGLE_OAUTH_CLIENT_USERINFO_URI = "/oauth2/v2/userinfo"


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
