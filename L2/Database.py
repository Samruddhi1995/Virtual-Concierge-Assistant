import json
import boto3
def PutItem(SuggestionsList,MessageId):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Restaurantdata')
    SuggestionsList = json.dumps(SuggestionsList)
    print(type(SuggestionsList))
    dict = {'identity' : MessageId,'SuggestionsList' : SuggestionsList}
    table.put_item(Item=dict)
    