import os 
from dotenv import load_dotenv


class Config:
    
    SQLALCHEMY_DB_URI='postgresql+psycopg2://moringa:kenyan@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    

class DevConfig(Config):
    '''
    Develop cofiguration class for child
    '''
    SQLALCHEMY_DATABASE_URI =os.environ.get('SQLALCHEMY_DATABASE_URI')

    Debug=True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DB")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:password@kenyan/blog_test'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI =os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True

config_options={
    'development': DevConfig, 
    'production':ProdConfig,
    'test':TestConfig 
    }