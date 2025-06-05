import os
import boto3

# Set your bucket name and destination folder
BUCKET_NAME = 'l3extra'
DEST_FOLDER = 'bucketfiles'

# Create destination folder if it doesn't exist
os.makedirs(DEST_FOLDER, exist_ok=True)

# Initialize S3 client
s3 = boto3.client('s3')

# List all objects in the bucket
response = s3.list_objects_v2(Bucket=BUCKET_NAME)

if 'Contents' in response:
    for obj in response['Contents']:
        key = obj['Key']
        dest_path = os.path.join(DEST_FOLDER, key)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        print(f'Downloading {key} to {dest_path}...')
        s3.download_file(BUCKET_NAME, key, dest_path)
else:
    print('No files found in the bucket.')