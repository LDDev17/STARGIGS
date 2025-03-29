from flask import Blueprint
from app.Blueprint.clients.controllers import register_new_client, get_client, update_client, delete_client, get_all_clients


client_blueprint = Blueprint('client_bp', __name__)


client_blueprint.route('/', methods=['POST'])(register_new_client)
client_blueprint.route('/<int:id>', methods=['GET'])(get_client)  
client_blueprint.route('/<int:id>', methods=['PUT'])(update_client)  
client_blueprint.route('/<int:id>', methods=['DELETE'])(delete_client) 
client_blueprint.route('/', methods=['GET'])(get_all_clients)  