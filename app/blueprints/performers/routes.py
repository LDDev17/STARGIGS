from flask import Blueprint
from performers.controllers import delete_my_performer_profile, get_all, complete_performer_profile, get_performer_profile, update_performer_profile

performers_blueprint = Blueprint('performers_bp', __name__)

performers_blueprint.route('/', methods=['POST'])(complete_performer_profile)  
performers_blueprint.route('/<int:id>', methods=['GET'])(get_performer_profile) 
performers_blueprint.route('/<int:id>', methods=['PUT'])(update_performer_profile) 
performers_blueprint.route('/<int:id>', methods=['DELETE'])(delete_my_performer_profile) 
performers_blueprint.route('/', methods=['GET'])(get_all) 