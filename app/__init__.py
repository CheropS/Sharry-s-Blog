from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from .config import config_options

db=SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):

    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
    
    from .main import main as main_blueprint
    
    app.register_blueprint(main_blueprint)
    db.init_app(app)
    login_manager.init_app(app)
   
    return app
