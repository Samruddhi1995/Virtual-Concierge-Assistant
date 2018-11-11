import http.client
import json
import urllib
import boto3
import datetime
import time
import Database
import pushsms


def getsuggestions(dinnerTime,cuisine,location,noOfPeople,phoneNo,Date,email,MessageId):
    
    headers = {'authorization': "Bearer idY3nVosr-23u6nRBvdjolhhbM5CE-qtc_LdnqWK1egdDz3WtugHtinMXeXM8V-Lz3nvV130N6DrDQpy2dBbPmy5ZB93OMjPU1a8mdD--Dj8DL4N8CTXQ3qdF-HhW3Yx"}
    
    dd = Date.replace('-', ',')
    hh = dinnerTime.replace(':', ',')
    dd = dd.split(',')
    hh = hh.split(',')
        
    print('here') 
    print(dd, hh)

    dt = datetime.datetime(2018, int(dd[1]), int(dd[2]), int(hh[0]), int(hh[1]))
    #print(str(time.mktime(dt.timetuple()))) 
    timestamp = dt.strftime("%s")
    print(timestamp)
    
    params = {'location':location, 'categories':"restaurants,"+cuisine,'term':cuisine, "limit":"5", 'open_at' : timestamp,'radius':"1000"}
    
    
    param_string = urllib.parse.urlencode(params)
    
    print(param_string)
    conn = http.client.HTTPSConnection("api.yelp.com") 
    conn.request("GET", "/v3/businesses/search?"+param_string, headers=headers)
 
    res = conn.getresponse() 
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    print(json.dumps(data))
    suggestions = dict()
    SuggestionsList = list()
    
    try:
        for i in range(0,3):
            try:
                title = data['businesses'][i]['categories'][0]['title']
            except KeyError:
                title = "NA"
            try:
                name = data['businesses'][i]['name']
            except KeyError:
                name = "NA" 
            try:
                price = data['businesses'][i]['price']
            except KeyError:
                price = "NA"
            try:
                rating = data['businesses'][i]['rating'] 
            except KeyError:
                rating = "NA"
            try:
                address = data['businesses'][i]['location']['address1']
            except KeyError:
                address = "NA"
           
            suggestions = {'title':title, 'name':name, 'price':price, 'rating':rating, 'address':address}
            SuggestionsList.append(suggestions)
            print(SuggestionsList)
    except:
        pass
        
    pushsms.sendsms(SuggestionsList,phoneNo,email)
    Database.PutItem(SuggestionsList,MessageId)