from flask import Flask
from flask_cors import CORS
from database import db
from app.models.schemas import ma
from app.extensions import socketio


from app.blueprints.auth.routes import auth_bp
from app.blueprints.booking.routes import booking_blueprint
from app.blueprints.client.routes import client_blueprint
from app.blueprints.payments.routes import payments_blueprint
from app.blueprints.performers.routes import performers_blueprint
from app.blueprints.reviews.routes import review_bp
from app.blueprints.search.routes import search_blueprint
from app.blueprints.messaging.routes import messaging_blueprint

from instance.config import DevelopmentConfig, TestingConfig, ProductionConfig

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

    @app.route("/")
    def hello_world():
        return "<h1>Welcome to STARGIGS!</h1>"

    db.init_app(app)
    ma.init_app(app)
    CORS(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(booking_blueprint, url_prefix='/booking')
    app.register_blueprint(client_blueprint, url_prefix='/client')
    app.register_blueprint(payments_blueprint, url_prefix='/payments')
    app.register_blueprint(performers_blueprint, url_prefix='/performers')
    app.register_blueprint(review_bp, url_prefix='/reviews')
    app.register_blueprint(search_blueprint, url_prefix='/search')
    app.register_blueprint(messaging_blueprint, url_prefix='/messaging')

    with app.app_context():
        db.create_all()

    print('\nSTARGIGS APP is Running\n')

    socketio.init_app(app)

    return app