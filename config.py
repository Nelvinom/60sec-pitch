import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):

    # SECRET_KEY = os.environ.get('SECRET_KEY') 
    SECRET_KEY = 'c04d7bf36bfb9de2166125a6'
    #  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:72330000@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX = 'Pitches'
class ProductionConfig(Config):
     pass
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class DevelopmentConfig(Config):
    # DEVELOPMENT = True
    DEBUG = True
class TestingConfig(Config):
    TESTING = True
config_options = {
'test':TestingConfig,
'development':DevelopmentConfig
}