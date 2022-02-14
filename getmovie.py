from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def get_movie(title,year,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    
    table = dynamodb.Table('Movies')

    try:
        response = table.get_item(Key={'year': year, 'title': title})

        

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response

if __name__ == '__main__':
    movie = get_movie("Kung fu", 2004,)
    if movie:
        print("get succeeded")
        pprint(movie, sort_dicts=False)
