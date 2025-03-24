from flask import Flask
from database import db
from app.models.schemas import ma
from config import config

from app.Blueprint.auth.routes import auth_blueprint
from app.Blueprint.booking.routes import booking_blueprint
from app.Blueprint.clients.routes import client_blueprint
from app.Blueprint.payments.routes import payments_blueprint
from app.Blueprint.performers.routes import performers_blueprint
from app.Blueprint.reviews.routes import reviews_blueprint
from app.Blueprint.search.routes import search_blueprint

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    @app.route("/")
    def hello_world():
        return "<h1>Welcome to STARGIGS , Your App is working!</h1>"
    
    
    db.init_app(app)  # Initialize SQLAlchemy
    ma.init_app(app)  # Initialize Marshmallow

    #Registering blueprints
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(booking_blueprint, url_prefix='/booking')
    app.register_blueprint(client_blueprint, url_prefix='/client')
    app.register_blueprint(payments_blueprint, url_prefix='/payments')
    app.register_blueprint(performers_blueprint, url_prefix='/performers')
    app.register_blueprint(reviews_blueprint, url_prefix='/reviews')
    app.register_blueprint(search_blueprint, url_prefix='/search')

    
    with app.app_context():
        db.create_all()  # Ensure tables are created

    print()
    print('STARGIGS APP is Running')
    print()

    return app
