import serial
import pyttsx3
import time
import geocoder
import reverse_geocoder as rg
from real_time_object_detection import img_processing
global img_processing


def reverseGeocode(coordinates):
    result = rg.search(coordinates)
    pprint.pprint(result[0]["admin2"])
    address = result[0]["admin2"]
    print(address)
    return address


def object_detection(destination):
  ser = serial.Serial("/dev/ttyACM0", 9600)

  engine = pyttsx3.init()

  while True:
      if ser.inWaiting() > 0:
        x = ser.readline()
        y = str(x.decode().strip())
        r = img_processing()
        engine.say("here is " + r + "with a distance of" + y + "at u")
        engine.runAndWait()
        time.sleep(1)
        g = geocoder.ip('me')
        newcoordinates = (g.lat, g.lng)
        address = reverseGeocode(newcoordinates)
        if address == destination:
          engine.say("You are at location"+destination+"Successfully reached")
          engine.runAndWait()
