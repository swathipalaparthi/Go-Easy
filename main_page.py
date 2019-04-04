import pyttsx3 as pyt
import speech_recognition as sr
import geocoder
import reverse_geocoder as rg 
import pprint 
from geolocation.main import GoogleMaps 
from geolocation.distance_matrix.client import DistanceMatrixApiClient
# importing googlemaps module 
import googlemaps 
from arduinoopin import object_detection

global object_detection

def reverseGeocode(coordinates): 
    result = rg.search(coordinates) 
    pprint.pprint(result)	
    pprint.pprint(result[0]["name"]) 
    address = result[0]["name"]
    print(address)
    return address

"""def getDestination():
    re = sr.Recognizer()
    with sr.Microphone() as dest:
        audio = re.listen(dest)

    try:
        test = re.recognize_google(audio)
        print('you said:{}',format(test))
        engine.say("You said ",test)
        engine.runAndWait()
        return test
    except:
        print('Sorry')
        engine.say("Sorry time up")
        engine.runAndWait()
        return "0"
"""
engine =  pyt.init()
engine.say("hi Welcome to go easy mania.   Please wait we are fetching your current location")
engine.runAndWait()
g = geocoder.ip('me')
newcoordinates = (g.lat,g.lng)	
address = reverseGeocode(newcoordinates)  
# print("add",address)
source = address
engine.say("Your current location is"+source)
engine.runAndWait()
engine.say("please say your  destination location")
engine.runAndWait()

"""destination = getDestination()
while destination == "0":
    destination = getDestination()"""
destination = str(input())
"""

# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyCHhUlpS70SGAFqQfFjrnRwkixFxLGUpl4') 

# Requires cities name 
my_dist = gmaps.distance_matrix(source,destination)['rows'][0]['elements'][0] 

# Printing the result 
print(my_dist) 
engine.say(my_dist)
engine.runAndWait()
"""
engine.say("Are you ready to start your journey")
engine.runAndWait()

input1 = input("enter yes")
if  input1 == "yes":
    engine.say("Start your journey. Obstacles will be deteced")
    engine.runAndWait()
    object_detection(destination)

else:
    engine.say("cannot start your journey")
    engine.runAndWait()

