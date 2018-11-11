import json
import boto3
def PostReq(message):
    response = client = boto3.client('lex-runtime')
    print(message)
    response = client.post_text( botName='restaurantdetails', botAlias='$LATEST',   userId='USER' ,inputText=message)
    #print(response['message'])
    return(response['message'])
