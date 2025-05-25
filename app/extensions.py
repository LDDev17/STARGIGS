from flask_socketio import SocketIO
from flask_mail import Mail
socketio = SocketIO(cors_allowed_origins="*", async_mode="eventlet")



mail = Mail()
