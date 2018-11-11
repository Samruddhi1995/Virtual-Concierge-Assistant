import json
import boto3
import sqspop
def lambda_handler(event, context):
    #print("worker lambda was called")
    # TODO implement
    
    #sns = boto3.client('sns',region_name="us-east-1")
    #number = '+19173730847'
    #sns.publish(PhoneNumber = number, Message='example text message' )
    #print("hey")
    sqspop.sqspop()
    
    
    
    
    
    