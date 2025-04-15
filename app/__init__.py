from flask import Flask
from database import db
from app.models.schemas import ma
from instance.config import config
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Marshmallow


db=SQLAlchemy()  # Initialize SQLAlchemy
ma=Marshmallow()  # Initialize Marshmallow



def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    @app.route("/")
    def hello_world():
        return "<h1>Welcome to STARGIGS , Your App is working!</h1>"
    
    
    db.init_app(app)  # Initialize SQLAlchemy
    ma.init_app(app)  # Initialize Marshmallow

    with app.app_context():
        db.create_all()  # Ensure tables are created

    print()
    print('STARGIGS APP is Running')
    print()

    return app
