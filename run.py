from app import create_app, socketio
import os

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    # Determine debug mode from environment variable
    debug_mode = os.getenv("FLASK_DEBUG", "FALSE") == "True"
    # Run the app using Flask-SocketIO
    socketio.run(app, debug=debug_mode)