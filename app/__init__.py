from flask import Flask
from database import db
from app.models.schemas import ma
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)  # Initialize SQLAlchemy
    ma.init_app(app)  # Initialize Marshmallow

    with app.app_context():
        db.create_all()  # Ensure tables are created

    print('STARGIGS APP is Running')

    return app
