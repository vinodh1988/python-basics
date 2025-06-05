import json
import boto3

# List of person dictionaries
persons = [
    {"sno": 1, "name": "Alice", "city": "New York"},
    {"sno": 2, "name": "Bob", "city": "Los Angeles"},
    {"sno": 3, "name": "Charlie", "city": "Chicago"}
]



# Write the JSON array to person.json
with open("person.json", "w") as f:
    json.dump(persons,f,indent=4)

# Upload person.json to S3 bucket 'l3extra'
s3 = boto3.client('s3')
with open("person.json", "rb") as data:
    s3.upload_fileobj(data, "l3extra", "person.json")
    #s3.upload_file((fileobject,bucketname,filename))

print("person.json uploaded to S3 bucket 'l3extra'.")