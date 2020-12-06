import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('REST')
    
    userId = event['Id']
    firstName = event['FirstName']
    
    try:
        response = table.delete_item(
            Key={
                    'Id': userId,
                    'FirstName': firstName
                }
        )
        return response
    except Exception as e:
        print(e)
        return {
                'statusCode': 400,
                'body': json.dumps('Error dele the user info')
        }
