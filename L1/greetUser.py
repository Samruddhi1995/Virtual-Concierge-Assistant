import lexResponses
def greetUser(intentRequest):
    source = intentRequest["invocationSource"]
    if (source == 'DialogCodeHook'):
        return lexResponses.close(intentRequest["sessionAttributes"], 'Fulfilled', "Hi there, how can I help?")