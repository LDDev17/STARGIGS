import boto3
import os
from werkzeug.utils import secure_filename
import uuid

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("S3_REGION")
)

def upload_file_to_s3(file, folder="profile_pictures"):
    bucket = os.getenv("S3_BUCKET_NAME")
    filename = secure_filename(file.filename)
    unique_filename = f"{folder}/{uuid.uuid4()}_{filename}"
    
    try:
        s3.upload_fileobj(
            file,
            bucket,
            unique_filename,
            ExtraArgs={"ACL": "public-read", "ContentType": file.content_type}
        )
        file_url = f"https://{bucket}.s3.amazonaws.com/{unique_filename}"
        return file_url
    except Exception as e:
        raise Exception(f"Upload failed: {str(e)}")