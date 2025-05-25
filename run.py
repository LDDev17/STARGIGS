import os
from app import create_app, socketio
from flask_migrate import Migrate
from flask.cli import with_appcontext
from database import db
from app.models import *  # Ensure all models are imported for Alembic

app = create_app()
migrate = Migrate(app, db)

if os.environ.get("FLASK_ENV") == "development":
    app.debug = True

if __name__ == "__main__":
    # You can toggle debug as needed
    socketio.run(app, host="0.0.0.0", port=5000)