import json 
import boto3
def sendsms(SuggestionsList,phoneNo,email):
    print(SuggestionsList,phoneNo)
    xyz = 'Hello Here are my suggestions: \n'
    for i in SuggestionsList: 
       xyz = xyz + (" title "+ i['title']) + " name "+ (i['name'])+ " price " + (i['price'])+ " address " +(i['address'])+ " rating "+ str(i['rating']) + "\n"
       
    print(xyz)
    print(email)
    client=boto3.client('sns')
    client.subscribe(TopicArn = 'arn:aws:sns:us-east-1:710893033804:RestaurantSuggestions',Protocol='Email',Endpoint=email)
    response = client.publish(TopicArn = 'arn:aws:sns:us-east-1:710893033804:RestaurantSuggestions',Message=xyz)
    print("SNS RESPONSE")
    print(response)
    print("SNS RESPONSE END")

    #response = client.unsubscribe(SubscriptionArn=response["SubscriptionArn"])