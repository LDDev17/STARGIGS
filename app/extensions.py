

from flask_socketio import SocketIO
from flask_mail import Mail
socketio = SocketIO(cors_allowed_origins="*", async_mode="eventlet")

# Initialize Flask-Mail extension
mail = Mail()