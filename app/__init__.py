from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from .config import config_options
from flask_bootstrap import Bootstrap
from flask_mail import Mail

db=SQLAlchemy()
login_manager = LoginManager()
bootstrap=Bootstrap()
login_manager_protection = 'strong'
login_manager.login_view = 'auth.login'
mail=Mail()

def create_app(config_name):

    #Initializing application
    app=Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    
    from .main import main as main_blueprint
    from .auth import auth

    # Initializing Flask Extensions
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth, url_prefix='/authenticate')

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
   
    return app
