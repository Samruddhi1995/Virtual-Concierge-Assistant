import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
import callinglex

def lambda_handler(event, context):
    #print("This is it")   
    #print(type(event))
    #print("This")
    #logger.info('got event{}'.format(event))
    # dic = { 'Hi' : 'Hello, How can I help you?', 'Good morning' : 'Good morning, Need help?' } 
    # if dic.has_key('Hi'):
    # message = dic.get('Hi')
    #print(event["messages"][0]["unstructured"]["text"])
    #reply = return_messages(event["messages"][0]["unstructured"]["text"])
    
    try:
        
        response = callinglex.PostReq(event["messages"][0]["unstructured"]["text"])
        
    except:
         
         response = "There was some error is delivering the response. Please start over"
    
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
    


