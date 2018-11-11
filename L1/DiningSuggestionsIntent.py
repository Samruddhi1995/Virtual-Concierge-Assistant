import lexResponses
import sqspush
import json

def try_ex(func):
    """
    Call passed in function in try block. If KeyError is encountered return None.
    This function 
    ended to be used to safely access dictionary.

    Note that this function would have negative impact on performance.
    """

    try:
        return func()
    except KeyError:
        return None





    

def DiningSuggestionsIntent(intent_request):
    
    
    print(json.dumps(intent_request))
    source = intent_request["invocationSource"]
    '''
    location = try_ex(lambda: intent_request['currentIntent']['slots']['location'])
    cuisine = try_ex(lambda: intent_request['currentIntent']['slots']['cuisine'])
    noofpeople = try_ex(lambda: intent_request['currentIntent']['slots']['noOfPeople'])
    phoneno = try_ex(lambda: intent_request['currentIntent']['slots']['phoneNo'])
    time = try_ex(lambda: intent_request['currentIntent']['slots']['dinnerTime'])
    
    '''
    if intent_request['invocationSource'] == 'DialogCodeHook':
        session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
        # Validate any slots which have been specified.  If any are invalid, re-elicit for their value
        
        '''validation_result = validate_input(intent_request['currentIntent']['slots'])
        if not validation_result['isValid']:
            slots = intent_request['currentIntent']['slots']
            slots[validation_result['violatedSlot']] = None

            return elicit_slot(
                session_attributes,
                intent_request['currentIntent']['name'],
                slots,
                validation_result['violatedSlot'],
                validation_result['message']
            )'''
            
            
        delegateResponse = lexResponses.delegate(session_attributes, intent_request['currentIntent']['slots'])
        print("delegateResponse")
        print(delegateResponse)
        return delegateResponse
        
    if (source == 'FulfillmentCodeHook'):
        sqspush.sqspush(intent_request)
        return lexResponses.close(intent_request["sessionAttributes"], 'Fulfilled', "You are all set. Expect my recommendations shortly! Have a good day.")