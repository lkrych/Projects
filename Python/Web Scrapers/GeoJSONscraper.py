'''In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py. 
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
'''
import json
import urllib

serviceurl = 'http://python-data.dr-chuck.net/geojson?' #api created by Dr. Chuck


#address = raw_input('Enter location: ')
#if len(address) < 1 : break

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': 'King Mongkuts University of Technology Thonburi'}) #properly encode url
print 'Retrieving', url
uh = urllib.urlopen(url) #create connection to url
data = uh.read() #read data from connection
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data)) #load the json as a string
except: js = None
if 'status' not in js or js['status'] != 'OK':
    print '==== Failure To Retrieve ===='
    print data
    #continue

print json.dumps(js, indent=4) #investigate the json architecture

print js['results'][0]['place_id'] #index for place_id based on json architecture
