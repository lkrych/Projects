# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    ''' This class contains five components:
globally unique identifier (GUID) - a string that serves as a unique name for this entry

title - a string

subject - a string

summary - a string

link to more content - a string
    '''
    def __init__(self, guid, title, subject, summary, link):
        """Create an empty set of integers"""
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    
    def getGuid(self):
        return self.guid
    def getTitle(self):
        return self.title
    def getSubject(self):
        return self.subject
    def getSummary(self):
        return self.summary
    def getLink(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger): #subclass of the trigger, this subclass is never directly called, but provides isWordin function for subclasses
    ''' Analyzes texts for occurence of word in text, texts are defined in subclasses.
        also, strips punctuation and turns letters into lowercase
    '''    
    def __init__(self, word): #This subclass has two stored objects, whatever is passed to it 'self' and word, the word is what is being checked against
               
        self.myWord = word.lower() #init new attribute word, make it lowercase
    
    def getWord(self): #define a method to getWord so you don't have to access it directly
        return self.myWord
        
    def isWordin(self,text): #Very important! checks your text for instance of word!
        repl =  text.replace("'",' ') #replaces all apostrophes with spaces, it's difficult to rid strings of their apostrophes in the next line
        noPunct = repl.translate(None,string.punctuation).lower() #removes punctuation
        checkList = noPunct.split() #split strings into lists
        if self.myWord in checkList: #check over list for word
            return True
        else:
            return False

class TitleTrigger(WordTrigger): #subclass of Wordtrigger, redefines evaluate to look into specific aspects of NewsStory class
    def evaluate(self, story):
        self.myStory = story
        
        return self.isWordin(self.myStory.getTitle())
        
class SubjectTrigger(WordTrigger): #see title trigger
    def evaluate(self, story):
        self.myStory = story
        
        return self.isWordin(self.myStory.getSubject())
        
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        self.myStory = story
        
        return self.isWordin(self.myStory.getSummary())


# Composite Triggers
# Problems 6-8

class NotTrigger(Trigger): #NotTriggers are subclasses of the trigger type, this set of triggers is similar to those above except that they are NOT word triggers. 
    def __init__(self, trigger1):  #These triggers fire after they logically evaluate the behavior of word Triggers. For instance, this not trigger fires if a wordTrigger does not fire!
        self.myTrigger = trigger1
        
    def evaluate(self,story): #Need to redefine your evaluate definition because it is unusable in your Trigger class
        return not self.myTrigger.evaluate(story) 
    
    
class AndTrigger(Trigger): #See explanation of nottrigger, 
    def __init__(self, trigger1, trigger2):
        self.myTrigger1 = trigger1
        self.myTrigger2 = trigger2
    def evaluate(self,story):
        return self.myTrigger1.evaluate(story) and self.myTrigger2.evaluate(story)

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.myTrigger1 = trigger1
        self.myTrigger2 = trigger2
    def evaluate(self,story):
        return self.myTrigger1.evaluate(story) or self.myTrigger2.evaluate(story)


# Phrase Trigger
# Question 9

class PhraseTrigger(Trigger): #searches for a phrase in title, subject or summary
    def __init__(self, phrase):
        self.myPhrase = phrase
    
    def evaluate(self,story):
        self.myTitle = story.getTitle()
        self.mySubject = story.getSubject()
        self.mySummary = story.getSummary()
        return self.myPhrase in self.myTitle or self.myPhrase in self.mySubject or self.myPhrase in self.mySummary
    


#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist): #simple nested loops to return stories which had a trigger fire on them
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    newsStories = []    
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                newsStories.append(story)
                break
    return newsStories
        
        
        
    
    

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name): #perhaps the most confusing part of the code you defined yourself. This code saves instances of triggers in a dictionary and then presents them to a function below this one.
    """
    Takes in a map of names to trigger instance, the type of trigger to make, #The purpose of this code is to allow you to modulate the triggers you want to search for without directly accessing the code. 
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    if triggerType == 'TITLE':
        triggerMap[name] = TitleTrigger(params[0]) 
    if triggerType == 'SUBJECT':
        triggerMap[name] = SubjectTrigger(params[0])
    if triggerType == 'SUMMARY':
        triggerMap[name] = SummaryTrigger(params[0])
    if triggerType == 'OR':
        triggerMap[name] = OrTrigger((triggerMap[params[0]]), (triggerMap[params[1]]))
    if triggerType == 'AND':
        triggerMap[name] = AndTrigger((triggerMap[params[0]]), (triggerMap[params[1]]))
    if triggerType == 'NOT':
        triggerMap[name] = NotTrigger(triggerMap[params[0]])
    if triggerType == 'PHRASE':
        triggerMap[name] = PhraseTrigger(' '.join(params))
    return triggerMap[name]


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        # triggerlist = readTriggerConfig("triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

