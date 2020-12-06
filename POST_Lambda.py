import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    
    tableREST = dynamodb.Table('REST')
    
    # {"Id": "a1", "FirstName": "Robert", "LastName": "Downy", "Age": 45, "Hobbies": ["Movies", "Books"]}
    eventDateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    userId = event['Id']
    firstName = event['FirstName']
    lastName = event['LastName']
    age = event['Age']
    hobbies = event['Hobbies']
    
    try:
        
        tableREST.put_item(
           Item={
                'eventDateTime': eventDateTime,
                'Id': userId,
                'FirstName': firstName,
                'LastName': lastName,
                'Age': age,
                'Hobbies': hobbies
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully inserted the user info!')
        }
    except:
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving the user info')
        }
