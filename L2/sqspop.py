import json

import boto3
import ExtractInfo
def sqspop():
    sqs = boto3.client('sqs')
    QueueUrl = sqs.get_queue_url(QueueName='orders')
    QueueUrl= QueueUrl['QueueUrl']
    response = sqs.receive_message(QueueUrl=QueueUrl,MaxNumberOfMessages=10)
    #print("response")
    print(json.dumps(response))
    
    try:
        print(len(response["Messages"]))
        
        for i in range(0,len(response["Messages"])):
            print(i)
            MessageId = (response["Messages"][i]["MessageId"])
            body = (response["Messages"][i]["Body"])
            ReceiptHandle = (response["Messages"][i]["ReceiptHandle"])
            body = json.loads(body)
            slots = body["currentIntent"]["slots"]
            print("slots")
            print(slots)
            delete_reply = sqs.delete_message( QueueUrl=QueueUrl,ReceiptHandle=ReceiptHandle)
            print(delete_reply)
            ExtractInfo.ExtractInfo(slots,MessageId)
    except:
        return 0
        
    #print("body")
    #print(body)
    #ReceiptHandle = (response["Messages"][0]["ReceiptHandle"])
    #print("Receipt Handle")
    #print(ReceiptHandle)
    
    #body = json.loads(body)
    #slots = body["currentIntent"]["slots"]
    
    #print("Slots")
    #print(slots)
    
    #delete_reply = sqs.delete_message( QueueUrl=QueueUrl,ReceiptHandle=ReceiptHandle)
    #print(delete_reply)
    
    #ExtractInfo.ExtractInfo(slots,MessageId)
    
    
    
   