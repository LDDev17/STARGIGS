from flask import Blueprint
from app.modules.performers.controllers import ( 
    delete_my_performer_profile, 
    get_all, 
    complete_performer_profile, 
    get_performer_profile, 
    update_performer_profile
)

# Blueprint for performer-related routes
performers_blueprint = Blueprint('performers_bp', __name__)

# Route to retrieve all performers
performers_blueprint.route('/', methods=['GET'])(get_all) 

# Route to get the current performer's profile
performers_blueprint.route('/me', methods=['GET'])(get_performer_profile) 

# Route to create or complete the current performer's profile
performers_blueprint.route('/me', methods=['POST'])(complete_performer_profile)

# Route to update the current performer's profile
performers_blueprint.route('/me', methods=['PUT'])(update_performer_profile) 

# Route to delete the current performer's profile
performers_blueprint.route('/me', methods=['DELETE'])(delete_my_performer_profile)