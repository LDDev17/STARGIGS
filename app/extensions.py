from flask_socketio import SocketIO
from flask_mail import Mail

# Initialize SocketIO with CORS allowed for all origins
socketio = SocketIO(cors_allowed_origins="*")

# Initialize Flask-Mail extension
mail = Mail()