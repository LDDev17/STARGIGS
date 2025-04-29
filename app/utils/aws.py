

import boto3

def get_reviews_table():
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1") 
    return dynamodb.Table("Reviews")
