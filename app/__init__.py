from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from .config import config_options
from flask_bootstrap import Bootstrap

db=SQLAlchemy()
login_manager = LoginManager()
bootstrap=Bootstrap()

def create_app(config_name):

    #Initializing application
    app=Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    
    from .main import main as main_blueprint

    # Initializing Flask Extensions
    app.register_blueprint(main_blueprint)
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
   
    return app
