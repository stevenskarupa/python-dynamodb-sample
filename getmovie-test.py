import boto3
import json
from botocore.exceptions import ClientError
from decimal import Decimal
from pprint import pprint

def to_serializable(val):
    if isinstance(val, Decimal):
        return str(val)
    return val

def get_movie(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    
    table = dynamodb.Table('Movies')

    try:
     
        year = 2004
        title = 'Kung fu'

        data = table.get_item(Key={'year': year, 'title': title})
        #pprint(data, sort_dicts=False)

        s = json.dumps(data, default=to_serializable)
        pprint(s, sort_dicts=False)

        response = {
            'statusCode':200,
            'body': s,
            'headers': {
                'Content-Type':'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response

if __name__ == '__main__':
    movie = get_movie()
    pprint(movie, sort_dicts=False)

    
 