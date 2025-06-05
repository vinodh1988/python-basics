import boto3

# Create a session using default AWS credentials and region
s3 = boto3.client('s3')

# List all buckets
response = s3.list_buckets()
#pint(response)

print("S3 Buckets:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']} (created on {bucket['CreationDate']})")
