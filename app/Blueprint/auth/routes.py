from flask import Blueprint
#from auth.controllers import register, login, logout

auth_blueprint = Blueprint('auth_bp', __name__)

auth_blueprint.route('/register', methods=['POST'])#(register)
auth_blueprint.route('/login', methods=['POST'])#(login)
auth_blueprint.route('/logout', methods=['POST'])#(logout)