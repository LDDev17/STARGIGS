from flask import Blueprint
from app.services.search.controllers import search_performers_controller

# Blueprint for search-related routes
search_blueprint = Blueprint('search_bp', __name__)

# Route to search for performers based on query parameters
search_blueprint.route('/', methods=['GET'])(search_performers_controller)