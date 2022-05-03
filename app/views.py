from flask import render_template
from app import app
from .request import get_articles, get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_news()
    print(news_sources)
    title = 'Home'
    return render_template('index.html', title = title, sources = news_sources )

@app.route('/article')
def article():

    '''
    View root page function that returns the index page and its data
    '''
    top_article=get_articles()
    print(top_article)
    return render_template('article.html',articles= top_article)