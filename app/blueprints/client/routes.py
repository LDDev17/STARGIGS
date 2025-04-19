from flask import Blueprint
from app.blueprints.client.controllers import register_new_client, get_client_profile, update_client_profile, delete_client_account, get_all_clients


client_blueprint = Blueprint('client_bp', __name__)


client_blueprint.route('/', methods=['POST'])(register_new_client)
client_blueprint.route('/<int:id>', methods=['GET'])(get_client_profile)  
client_blueprint.route('/<int:id>', methods=['PUT'])(update_client_profile)  
client_blueprint.route('/<int:id>', methods=['DELETE'])(delete_client_account) 
client_blueprint.route('/', methods=['GET'])(get_all_clients)  