from flask import Blueprint
from app.Blueprint.auth.controllers import login_client_controller

auth_blueprint = Blueprint('auth_bp', __name__)


auth_blueprint.route('/login', methods=['POST'])(login_client_controller)
