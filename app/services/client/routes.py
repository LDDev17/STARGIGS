from flask import Blueprint
from app.services.client.controllers import register_new_client, get_client_profile, update_client_profile, delete_client_account 


client_blueprint = Blueprint('client_bp', __name__)


client_blueprint.route('/', methods=['POST'])(register_new_client)
client_blueprint.route('/me', methods=['GET'])(get_client_profile)  
client_blueprint.route('/me', methods=['PUT'])(update_client_profile)  
client_blueprint.route('/me', methods=['DELETE'])(delete_client_account) 
