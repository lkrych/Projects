#import flask framework
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#from flask_bootstrap import Bootstrap, how do you get bootstrap in flask?
app = Flask(__name__)

#import sqlalchemy to work with db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_newspaper import Base, Subject, Article

engine = create_engine('sqlite:///newspaper.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/subjects/<int:subject_id>/') #decorator will execute code that follows it if it detects
def subjectInfo(subject_id):
	subject = session.query(Subject).filter_by(id = subject_id).one()
	articles = session.query(Article).filter_by(subject_id = subject.id)
	return render_template('subject.html', subject = subject, items = articles)

#create route for new article
@app.route('/')
@app.route('/subjects/<int:subject_id>/new/', methods = ['GET', 'POST'])
def newArticle(subject_id):
	if request.method == 'POST':
		newItem = Article(headline = request.form.get('headline') , abstract = request.form.get('abstract') , source = request.form.get('source'), wordcount = request.form.get('wordcount') , url = request.form.get('url'), subject = subject_id)
		print newItem.headline
		session.add(newItem)
		session.commit()
		flash(str(newItem.name) + " was created!")
		return redirect(url_for('subjectInfo', subject_id = subject_id ))
	else:
		return render_template('newArticle.html', subject_id = subject_id)


if __name__ == '__main__':
	app.secret_key = "super_secret_key" #helps initiate "sessions" which allow for personalized experience on web page
	app.debug = True #server will reload every time you modify code
	app.run(host = '0.0.0.0', port = 5000)