import json
import boto3
from botocore.exceptions import ClientError

bucket_name = 'project-tl'
file_key = 'data.json'

s3 = boto3.client('s3')

 


employees = [
 { 'id': 1, 'name': 'Ashley' },
 { 'id': 2, 'name': 'Kate' },
 { 'id': 3, 'name': 'Joe' }
]

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
json_file_path = 'data.json'

#write_json(employees,json_file_path)
def read_json_from_s3(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    return json.loads(content)

data = read_json_from_s3(bucket_name, file_key)

