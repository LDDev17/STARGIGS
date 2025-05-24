# events.py

from flask import request
from flask_socketio import emit, join_room, leave_room
from app.extensions import socketio
from app import socketio


# Event handler for a new connection
@socketio.on('connect')
def handle_connect():
    print('User connected:', request.sid)

# Event handler for a new message
@socketio.on('send_message')
def handle_send_message(data):
    room = data['room']
    message = data['message']
    sender = data['sender_id']

    # Emit to the same room
    emit('receive_message', {'sender_id': sender, 'message': message}, room=room)

# Event handler for joining a room (e.g., for chat)
@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('joined', {'room': room}, room=room)

# Event handler for disconnect
@socketio.on('disconnect')
def handle_disconnect():
    print('User disconnected:', request.sid)
