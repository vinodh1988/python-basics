import boto3

# Replace with your bucket name and file details
bucket_name = 'l3extra'
object_key = 'Python_Frameworks.png'
download_path = 'Python_Frameworks.png'  # Local path to save the file

s3 = boto3.client('s3')

try:
    s3.download_file(bucket_name, object_key, download_path)
    print(f"Downloaded {object_key} from {bucket_name} to {download_path}")
except Exception as e:
    print(f"Error downloading file: {e}")