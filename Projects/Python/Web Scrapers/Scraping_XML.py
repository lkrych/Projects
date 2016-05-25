import urllib
import xml.etree.ElementTree as ET #save this library as ET

url = "http://python-data.dr-chuck.net/comments_171316.xml" #scrape data from this link
uh = urllib.urlopen(url) #use urllib to connect to website
data = uh.read() #use urllib to read data
tree = ET.fromstring(data) #convert data from url into string 
lst = tree.findall('comments/comment') #use ET method to find strings within these two classes
count = 0
for item in lst: 
    count += int(item.find('count').text) #convert string into integer
print count


