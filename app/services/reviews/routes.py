from flask import Blueprint
from .controllers import post_review, get_reviews

# Blueprint for review-related routes
review_bp = Blueprint("reviews", __name__, url_prefix="/reviews")

# Route to submit a new review
@review_bp.route("/", methods=["POST"])
def post_review_route():
    return post_review()

# Route to get all reviews for a specific performer
@review_bp.route("/<performer_id>", methods=["GET"])
def get_reviews_route(performer_id):
    return get_reviews(performer_id)