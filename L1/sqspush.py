import boto3
import json
def sqspush(intentRequest):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='orders')
    queue.send_message(MessageBody=json.dumps(intentRequest))
    return
