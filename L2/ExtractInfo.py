import json
import yelp 
def ExtractInfo(slots,MessageId):
    #print("Here is info: ")
    #print(slots)
    dinnerTime = slots["dinnerTime"]
    cuisine = slots["cuisine"]
    location = slots["location"]
    noOfPeople = slots["noOfPeople"]
    phoneNo = slots["phoneNo"]
    Date = slots["Date"]
    Email = slots["email"]
    print("dinnerTime: " + dinnerTime + " cuisine: " + cuisine + " location: " + location + " noOfPeople: " + noOfPeople + " phoneNo: " + phoneNo + " Date: "+"Date")
    yelp.getsuggestions(dinnerTime,cuisine,location,noOfPeople,phoneNo,Date,Email,MessageId)
  