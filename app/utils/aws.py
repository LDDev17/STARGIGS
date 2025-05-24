import boto3

# Utility function to get the DynamoDB Reviews table resource
def get_reviews_table():
    # Create a DynamoDB resource using boto3 for the specified AWS region
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1") 
    # Return the Reviews table object
    return dynamodb.Table("Reviews")