#import json
import json
import boto3

client = boto3.resource('dynamodb',region_name='us-east-1')
    

def lambda_handler(event, context):
    # TODO get the year and title from the context instead of hard coding it
    year = 2004
    title = 'Kung fu'

    table = client.Table('Movies')
    data = table.get_item(Key={'year': year, 'title': title})
    
    response = {
        'statusCode':200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    return response
