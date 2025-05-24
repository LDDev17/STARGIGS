from flask import Blueprint
from app.services.client.controllers import register_new_client, get_client_profile, update_client_profile, delete_client_account 

client_blueprint = Blueprint('client_bp', __name__)

# Route to register a new client
client_blueprint.route('/', methods=['POST'])(register_new_client)

# Route to get the current client's profile
client_blueprint.route('/me', methods=['GET'])(get_client_profile)  

# Route to update the current client's profile
client_blueprint.route('/me', methods=['PUT'])(update_client_profile)  

# Route to delete the current client's account
client_blueprint.route('/me', methods=['DELETE'])(delete_client_account)