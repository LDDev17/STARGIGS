from flask import Flask
# from flask_cors import CORS
from database import db
from app.models.schemas import ma
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask, render_template
from flask_mail import Mail
from app.extensions import socketio


from instance.config import DevelopmentConfig, TestingConfig, ProductionConfig

from app.services.auth.routes import auth_bp
from app.services.booking.routes import booking_blueprint
from app.services.client.routes import client_blueprint
from app.services.payments.routes import payments_blueprint
from app.services.performers.routes import performers_blueprint
from app.services.reviews.routes import review_bp
from app.services.search.routes import search_blueprint
from app.services.messaging.routes import messaging_blueprint
from app.services.gig_ads.routes import gig_ads_blueprint



db=SQLAlchemy()  # Initialize SQLAlchemy
ma=Marshmallow()  # Initialize Marshmallow

config_dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


def create_app(config_name='default'):
    app = Flask(__name__)
    # Make sure 'config' is imported or defined
    app.config.from_object(config_dict[config_name])
    mail = Mail()
    # CORS(app, supports_credentials=True)
    
    @app.route("/")
    def hello_world():
        return "<h1>Welcome to STARGIGS</h1>"
    
    
    db.init_app(app)  # Initialize SQLAlchemy
    ma.init_app(app)  # Initialize Marshmallow
    socketio.init_app(app) # Initialize SocketIO
    mail.init_app(app)# Initialize Flask-Mail
    
    
    #Registering blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(booking_blueprint, url_prefix='/bookings')
    app.register_blueprint(client_blueprint, url_prefix='/clients')
    app.register_blueprint(payments_blueprint, url_prefix='/payments')
    app.register_blueprint(performers_blueprint, url_prefix='/performers')
    app.register_blueprint(review_bp, url_prefix='/reviews')
    app.register_blueprint(search_blueprint, url_prefix='/search')
    app.register_blueprint(messaging_blueprint, url_prefix='/messaging')
    app.register_blueprint(gig_ads_blueprint, url_prefix='/gigs')
    

    with app.app_context():
        db.create_all()

    print('YOUR STARGIGS APP IS READY')    


    return app