from flask import Flask
from flask_cors import CORS
from database import db
from app.models.schemas import ma
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask, render_template
from flask_socketio import SocketIO


from app.blueprints.auth.routes import auth_bp
from app.blueprints.booking.routes import booking_blueprint
from app.blueprints.client.routes import client_blueprint
from app.blueprints.payments.routes import payments_blueprint
from app.blueprints.performers.routes import performers_blueprint
from app.blueprints.reviews.routes import review_bp
from app.blueprints.search.routes import search_blueprint
from app.blueprints.messaging.routes import messaging_blueprint



db=SQLAlchemy()  # Initialize SQLAlchemy
ma=Marshmallow()  # Initialize Marshmallow
socketio = SocketIO(cors_allowed_origins="*")  #Websocket



def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    
    @app.route("/")
    def hello_world():
        return "<h1>Welcome to STARGIGS , Your App is working!</h1>"
    
    
    db.init_app(app)  # Initialize SQLAlchemy
    ma.init_app(app)  # Initialize Marshmallow

    #Registering blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(booking_blueprint, url_prefix='/booking')
    app.register_blueprint(client_blueprint, url_prefix='/client')
    app.register_blueprint(payments_blueprint, url_prefix='/payments')
    app.register_blueprint(performers_blueprint, url_prefix='/performers')
    app.register_blueprint(review_bp, url_prefix='/reviews')
    app.register_blueprint(search_blueprint, url_prefix='/search')
    app.register_blueprint(messaging_blueprint, url_prefix='/messaging')

    CORS(app)

    with app.app_context():
        db.create_all()  # Ensure tables are created

    print()
    print('STARGIGS APP is Running')
    print()
    
    socketio.init_app(app)

    return app
