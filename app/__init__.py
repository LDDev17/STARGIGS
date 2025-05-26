import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from database import db  
from app.models.schemas import ma
from app.extensions import socketio, mail
from config import config

# Blueprints
from app.blueprints.auth.routes import auth_bp
from app.blueprints.booking.routes import booking_blueprint
from app.blueprints.client.routes import client_blueprint
from app.blueprints.payments.routes import payments_blueprint
from app.blueprints.performers.routes import performers_blueprint
from app.blueprints.reviews.routes import review_bp
from app.blueprints.search.routes import search_blueprint
from app.blueprints.messaging.routes import messaging_blueprint
from app.blueprints.gig_ads.routes import gig_ads_blueprint


migrate= Migrate()

def create_app():
    app = Flask(__name__)

    # Determine config from FLASK_ENV
    flask_env = os.getenv("FLASK_ENV", "default")
    env_config = config.get(flask_env, config["default"])
    app.config.from_object(env_config)


    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    socketio.init_app(app)
    mail.init_app(app)
    CORS(app, origins=os.getenv("CORS_ORIGINS", "*"))

    # Root route for health check
    @app.route("/")
    def hello_world():
        return "<h1>Welcome to STARGIGS</h1>"

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(booking_blueprint, url_prefix="/booking")
    app.register_blueprint(client_blueprint, url_prefix="/client")
    app.register_blueprint(payments_blueprint, url_prefix="/payments")
    app.register_blueprint(performers_blueprint, url_prefix="/performers")
    app.register_blueprint(review_bp, url_prefix="/reviews")
    app.register_blueprint(search_blueprint, url_prefix="/search")
    app.register_blueprint(messaging_blueprint, url_prefix="/messaging")
    app.register_blueprint(gig_ads_blueprint, url_prefix="/gigs")

  

    print("\n✅ YOUR STARGIGS APP IS READY\n")
    return app
