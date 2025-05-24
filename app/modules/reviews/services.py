from app.models.schemas.review_schema import create_review_item
from app.utils.aws import get_reviews_table
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def submit_review(data):
    """
    Handle creating a new review.
    Creates a review item and inserts it into the DynamoDB reviews table.
    Returns the created review item.
    """
    try:
        # Create the review item based on provided data
        review_item = create_review_item(
            performer_id=data["performer_id"],
            client_id=data["client_id"],
            rating=data["rating"],
            comment=data["comment"],
            event_type=data.get("event_type")
        )
        
        # Insert the review into DynamoDB
        table = get_reviews_table()
        table.put_item(Item=review_item)
        return review_item  # Return created review

    except ClientError as e:
        # Handle any exceptions during DynamoDB interaction
        print(f"Error inserting review: {e}")
        raise e

def get_reviews_for_performer(performer_id):
    """
    Retrieve all reviews for a specific performer.
    Queries the DynamoDB reviews table for reviews matching the performer_id.
    Returns a list of review items.
    """
    try:
        table = get_reviews_table()
        response = table.query(
            KeyConditionExpression=Key('performer_id').eq(performer_id)
        )
        return response["Items"]  # Return list of reviews

    except ClientError as e:
        print(f"Error fetching reviews: {e}")
        raise e