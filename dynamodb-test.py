# example from: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.01.html
# 

import boto3

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName':'year',
                'KeyType': 'HASH' #partition key
            },
            {
                'AttributeName':'title',
                'KeyType': 'RANGE' #sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName':'year',
                'AttributeType':'S'
            },
            {
                'AttributeName':'title',
                'AttributeType':'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits':10,
            'WriteCapacityUnits':10
        }
    )
    return table

if __name__ == '__main__':
    movie_table = create_movie_table()
    print("Table Status:", movie_table.table_status)