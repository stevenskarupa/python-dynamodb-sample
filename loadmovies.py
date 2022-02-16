# example from: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.01.html
# 
from decimal import Decimal
import boto3
import json

def load_movies(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.Table('Movies')
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie:", year, title)
        table.put_item(Item=movie)

if __name__ == '__main__':
    with open('moviedata.2.json') as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    load_movies(movie_list)

