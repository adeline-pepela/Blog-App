import os

class Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adeh:adeh123!@localhost/blogdb'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SECRET_KEY = 'adeh123'
  UPLOADED_PHOTOS_DEST ='app/static/photos'



class TestConfig(Config):
  pass

class ProdConfig(Config):
  pass

class DevConfig(Config):
  
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adeh:adeh123!@localhost/blogdb'
  
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production':ProdConfig
}