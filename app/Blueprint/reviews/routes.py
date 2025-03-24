from flask import Blueprint
#from reviews.controllers import add_review, get_reviews, delete_review

reviews_blueprint = Blueprint('reviews_bp', __name__)

reviews_blueprint.route('/', methods=['POST'])#(add_review)  
reviews_blueprint.route('/<int:performer_id>', methods=['GET'])#(get_reviews) 
reviews_blueprint.route('/<int:id>', methods=['DELETE'])#(delete_review)  