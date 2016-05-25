from BeautifulSoup import *
import urllib
import ssl #this library allows your python code to work on https pages... not sure how this works. 
ssl._create_default_https_context = ssl._create_unverified_context

def follow_Link(linkPos,repeat):
    '''
    This function has two parametrs, linkPos which is the position of the link in the url below, and the repeat parameter which asks how many times you want to follow the link that is returned from linkPOS
    Uses nested loops, the outer loop is controlled by repeat which specifies how many pages the function crawls,
    and the inner loop is controlled by linkPOS, when it gets to the right link it returns it to the outer loop to be followed
    '''
    
    url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Tomas.html "
    
    for index in range(repeat):
        
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
    
        # Retrieve all of the anchor tags
        tags = soup('a')
        count = 0
        for tag in tags:
            count+=1
            if count == linkPos:
                url = tag.get('href',None)
                break
        
    return url


