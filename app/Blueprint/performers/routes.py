from flask import Blueprint
#from performers.controllers import create_performers, get_performers, update_performers, delete_performers, upload_media, get_all_performers

performers_blueprint = Blueprint('performers_bp', __name__)

performers_blueprint.route('/', methods=['POST'])#(create_performers)  
performers_blueprint.route('/<int:id>', methods=['GET'])#(get_performers) 
performers_blueprint.route('/<int:id>', methods=['PUT'])#(update_performers) 
performers_blueprint.route('/<int:id>', methods=['DELETE'])#(delete_performers) 
performers_blueprint.route('/media/<int:id>', methods=['POST'])#(upload_media)
performers_blueprint.route('/', methods=['GET'])#(get_all_performers)  