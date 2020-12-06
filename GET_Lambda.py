import json
import boto3


def lambda_handler(event, context):  
    dynamodb = boto3.resource('dynamodb')  
    tableREST = dynamodb.Table('REST')  
    response = tableREST.scan()  
    return {    
                'statusCode': 200,    
                'body': response['Items']   
            }
