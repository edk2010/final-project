import json
import boto3
from botocore.exceptions import ClientError

bucket_name = 'project-tl'
file_key = 'data.json'
s3 = boto3.client('s3')

def lambda_handler(event, context):
    

    
    try:
        data = read_json_from_s3(bucket_name, file_key)
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error reading file from S3: {str(e)}")
        }
    

    # Safely get the queryStringParameters
    query_params = event.get('queryStringParameters', {})

    # Default to None if the specific query parameter is not found
    operation = query_params.get('operation')
    user_id = query_params.get('user_id')   

    user_name = query_params.get('user_name')
    
    
    match operation:
        case "check_id":import json
import boto3
from botocore.exceptions import ClientError

bucket_name = 'project-tl'
file_key = 'data.json'
s3 = boto3.client('s3')

def lambda_handler(event, context):
    

    
    try:
        data = read_json_from_s3(bucket_name, file_key)
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error reading file from S3: {str(e)}")
        }
    

    # Safely get the queryStringParameters
    query_params = event.get('queryStringParameters', {})

    # Default to None if the specific query parameter is not found
    operation = query_params.get('operation')
    user_id = query_params.get('user_id')
    user_name = query_params.get('user_name')
    
    
    match operation:
        case "check_id":
            message = get_user_by_user_id(data, user_id)
        
        case "check_name":
            message = get_user_by_user_name(data,user_name)
        case "add_user":
            result = add_user(data, user_name)
            if result:
                message = f"new user: '{user_name}' added succesfuly"
            else:
                message = f'something went wrong'
        case "remove":
            result = delete_user_by_user_id(data,user_id)
            if result:
                message = f"user_id: '{user_id}' was deleted succesfuly"
            else:
                message = f'something went wrong'
        case _ :
            message = "You do not have any acce"
            
    
    
    # You can add your business logic here
    # For demonstration, we will just return the received parameters
    response_body = {
        "receivedParam1": operation,
        "receivedParam2": user_id,
        "full_name": user_name,
        "Data": data,
        "message": message
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response_body),
        'headers': {
            'Content-Type': 'application/json'
        }
    }




# Function to read JSON data from S3
def read_json_from_s3(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    return json.loads(content)

# Function to write JSON data to S3
def write_json_to_s3(data, bucket, key):
    s3.put_object(Body=json.dumps(data, indent=4), Bucket=bucket, Key=key)
    return True

# Function to add a new user

        
def add_user(data,user_name):
    new_user = {}
    #employee = 'new5'

    new_user['id'] = get_maximum_id(data) + 1
    new_user['name'] = user_name
    data.append(new_user)
    write_json_to_s3(data, bucket_name, file_key)
    return True

def get_user_by_user_id(data, user_id):
    return next((e for e in data if e['id'] == int(user_id)), None) 
           
def get_user_by_user_name(data,user_name):
    return next((e for e in data if e['name'] == user_name), None)

def delete_user_by_user_id(data,user_id):

    user = get_user_by_user_id(data,user_id)
    if user is None:
        return None

    data = [e for e in data if e['id'] != int(user_id)]
    write_json_to_s3(data, bucket_name, file_key)
    return True

def get_maximum_id(data):
    existing_ids = [user.get('id', 0) for user in data]
    # Calculate the maximum ID
    max_id = max(existing_ids)
    return max_id
