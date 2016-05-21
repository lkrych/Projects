# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 11:23:46 2015

@author: Leland
"""
import string

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

class Trigger(object):
    def evaluate(self, story): #this function looks incomplete... It is! You define the evaluate function for each subclass below!
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError #is not raised when subclass methods are called!
        
class WordTrigger(Trigger): #subclass of the trigger, this subclass is never directly called, but provides isWordin function for subclasses
    ''' Analyzes texts for occurence of word in text, texts are defined in subclasses.
        also, strips punctuation and turns letters into lowercase
    '''    
    def __init__(self, word): #This subclass has two stored objects, whatever is passed to it 'self' and word, the word is what is being checked against
               
        self.myWord = word.lower() #init new attribute word, make it lowercase
    
    def getWord(self): #define a method to getWord so you don't have to access the word directly
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
        
class NotTrigger(Trigger):
    def __init__(self, trigger, story):
        self.myTrigger = trigger
        self.myStory = story
        
        return not self.myTrigger.evaluate(self.myStory)
        
#class AndTrigger(Trigger):
    
#class OrTrigger(Trigger):