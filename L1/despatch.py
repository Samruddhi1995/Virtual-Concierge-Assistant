import greetUser
import DiningSuggestionsIntent
def despatch(intentRequest):
    userId = intentRequest["userId"]
    intentName = intentRequest["currentIntent"]["name"]
    print(intentName + ' was called')
    if (intentName == 'GreetingIntent'):
        return greetUser.greetUser(intentRequest)
    elif (intentName == 'DiningSuggestionsIntent'):
        return DiningSuggestionsIntent.DiningSuggestionsIntent(intentRequest)
    raise Exception('Intent with name ' + intent_name + ' not supported')