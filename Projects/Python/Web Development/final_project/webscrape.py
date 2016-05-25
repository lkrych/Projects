from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_newspaper import Base, Subject, Article #import classes from databaseSetup file

engine = create_engine('sqlite:///newspaper.db') #lets program know which db engine to connect with
Base.metadata.bind = engine #makes connections between classes and corresponding tables in db

DBSession = sessionmaker(bind = engine) #creates a link between our code and the engine we created

session = DBSession()

#####################WEB SCRAPING COMPONENT############################
#Info from http://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial

from nytimesarticle import articleAPI

api = articleAPI('dad4ec569b4924e931a381a9d9d1edb5:16:75117993')\

obamaArticles = api.search( q = 'Obama', 
     fq = {'headline':'Obama', 'source':['The New York Times']}, 
     begin_date = 20141231 )

clintonArticles = api.search( q = 'Hillary Clinton', 
     fq = {'headline':'Hillary Clinton', 'source':['The New York Times']}, 
     begin_date = 20141231 )

def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = []
    for i in articles['response']['docs']:
        dic = {}
        
        dic['id'] = i['_id'].encode("utf8")
        
        if i['abstract'] is not None:
            dic['abstract'] = i['abstract']
        dic['headline'] = i['headline']['main']
        
        dic['desk'] = i['news_desk']
        
        	
        dic['source'] = i['source']
        
        dic['type'] = i['type_of_material']
       
        dic['url'] = i['web_url']
        
        
        dic['word_count'] = i['word_count']
        
        # locations
        locations = []
        for x in range(0,len(i['keywords'])):
            if 'glocations' in i['keywords'][x]['name']:
                locations.append(i['keywords'][x]['value'].encode("utf8"))
        dic['locations'] = locations
        # subject
        subjects = []
        for x in range(0,len(i['keywords'])):
            if 'subject' in i['keywords'][x]['name']:
                subjects.append(i['keywords'][x]['value'].encode("utf8"))
        dic['subjects'] = subjects   
        news.append(dic)
    return(news) 

newsObama = parse_articles(obamaArticles)
newsClinton = parse_articles(clintonArticles)



##########################END WEB SCRAPING COMPONENT#########################

#load data into database

firstSubject = Subject(name = "Obama")

secondSubject = Subject(name = "Hillary Clinton")

session.add_all([firstSubject,secondSubject])

def addArticles(listOfArticles, subjectName):
	'''
	Insert data scraped from articles into DB
	listofArticles uses output from parse_articles, subject 
	'''
	for article in listOfArticles:
		currentArticle = Article(headline = article.get('headline') , abstract = article.get('abstract') , source = article.get('source'), wordcount = article.get('word_count') , url = article.get('url'), subject = subjectName)
		session.add(currentArticle)
	session.commit()

addArticles(newsObama,firstSubject)
addArticles(newsClinton,secondSubject)
