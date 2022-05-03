from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_news()
    title = 'Home'
    return render_template('index.html', title = title, sources = news_sources )

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('news.html',id=news_id)