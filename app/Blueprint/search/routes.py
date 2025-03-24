from flask import Blueprint
#from search.controllers import search_talent, filter_talent

search_blueprint = Blueprint('search_bp', __name__)

search_blueprint.route('/', methods=['GET'])#(search_talent)  
search_blueprint.route('/filter', methods=['GET'])#(filter_talent) 