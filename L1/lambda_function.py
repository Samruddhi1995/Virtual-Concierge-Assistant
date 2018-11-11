import json
import despatch
def lambda_handler(event, context):
    print(json.dumps(event))
    # TODO implement
    #print(type(event))
    #print(event["userId"])
    response = despatch.despatch(event)
    return response
    
         
                  
