from flask import jsonify, request
from app.modules.reviews.services import submit_review, get_reviews_for_performer

# Endpoint to submit a new review
def post_review():
    """POST endpoint to submit a review."""
    data = request.json  # Get review data from request
    review_item = submit_review(data)  # Call the service to submit review
    return jsonify(review_item), 201

# Endpoint to fetch all reviews for a specific performer
def get_reviews(performer_id):
    """GET endpoint to fetch reviews for a performer."""
    reviews = get_reviews_for_performer(performer_id)  # Call service to get reviews
    return jsonify(reviews), 200