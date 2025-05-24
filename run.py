from app import create_app, socketio
import os
app = create_app()

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "FALSE")== "True"
    socketio.run(app, debug=True)
