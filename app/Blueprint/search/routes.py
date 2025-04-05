from flask import Blueprint
from search.controllers import search_performers_controller

search_blueprint = Blueprint('search_bp', __name__)

search_blueprint.route('/', methods=['GET'])(search_performers_controller)  
