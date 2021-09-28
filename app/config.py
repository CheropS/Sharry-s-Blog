import os 



class Config:
    SQLALCHEMY_DB_URI=''
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevConfig(Config):
    Debug=True


config_options={
    'development': DevConfig}