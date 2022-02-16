from decimal import Decimal
from pprint import pprint
import boto3

def update_movie(title, year, rating, plot, actors, dynamodb=None):
  if not dynamodb:
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    
  table = dynamodb.Table('Movies')

  response = table.update_item(
    Key={
      'year' : year,
      'title': title
    },
    UpdateExpression = "set info.rating=:r, info.plot=:p, info.actors=:a",
    ExpressionAttributeValues={
      ':r': Decimal(rating),
      ':p': plot,
      ':a': actors
    },
    ReturnValues="UPDATED_NEW"   
  )
  return response

if __name__ == '__main__':
  update_response = update_movie(
    "Gravity", 2013, "1.1", "Dumbest movie ever made", ["schmuck1", "Schmuck2", "Schmuck3"]
  )
  print("updated movie successfully")
  pprint(update_response, sort_dicts=False)
