import boto3
import json
import uuid

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTasks')

# Lambda handler
def lambda_handler(event, context):
    method = event['httpMethod']
    
    if method == 'GET':
        response = table.scan()
        tasks = response.get('Items', [])
        return {
            'statusCode': 200,
            'body': json.dumps(tasks),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
    elif method == 'POST':
        data = json.loads(event['body'])
        task_id = str(uuid.uuid4())
        item = {
            'task_id': task_id,
            'task': data['task']
        }
        table.put_item(Item=item)
        return {
            'statusCode': 201,
            'body': json.dumps({"message": "Task added successfully!", "task_id": task_id}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
    elif method == 'DELETE':
        data = json.loads(event['body'])
        task_id = data['task_id']
        table.delete_item(Key={'task_id': task_id})
        return {
            'statusCode': 200,
            'body': json.dumps({"message": "Task deleted successfully!"}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
