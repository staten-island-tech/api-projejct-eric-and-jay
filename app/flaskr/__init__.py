import os
from flask import Flask, render_template, request, redirect, url_for
import requests



apikey = "0ceda6ac81b04000b04ba28dc647b7ad"

def getHeadlines(category=" "):
    if category != " ":
        url = ("https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}".format(category, apikey))
        response = requests.get(url)
        return response.json()
    else:
        url = ("https://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(apikey))
        response = requests.get(url)
        return response.json()

def searchArticles(query):
    url = ("https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}".format(query, apikey))
    response = requests.get(url)
    return response.json()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/", methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            title = request.form['search']
            if not title:
                return
            else:
                return redirect(url_for('search',query=title))

        data = getHeadlines()

        if data['status'] == 'error':
            return render_template('error.html', error_message="Too many requests! API is on a cooldown. Come back later.")
        else:
            return render_template('index.html', articles=data['articles'])


    @app.route("/business", methods=['GET', 'POST'])
    def business():
        if request.method == 'POST':
            title = request.form['search']
            if not title:
                return
            else:
                return redirect(url_for('search',query=title))

        data = getHeadlines('business')
        if data['status'] == 'error':
            return render_template('error.html', error_message="Too many requests! API is on a cooldown. Come back later.")
        else:
            return render_template('business.html', articles=data['articles'])

    @app.route("/health", methods=['GET', 'POST'])
    def health():
        if request.method == 'POST':
            title = request.form['search']
            if not title:
                return
            else:
                return redirect(url_for('search',query=title))
        
        data = getHeadlines('health')
        if data['status'] == 'error':
            return render_template('error.html', error_message="Too many requests! API is on a cooldown. Come back later.")
        else:
            return render_template('health.html', articles=data['articles'])

    @app.route("/science", methods=['GET', 'POST'])
    def science():
        if request.method == 'POST':
            title = request.form['search']
            if not title:
                return
            else:
                return redirect(url_for('search',query=title))
        data = getHeadlines('science')
        if data['status'] == 'error':
            return render_template('error.html', error_message="Too many requests! API is on a cooldown. Come back later.")
        else:
            return render_template('science.html', articles=data['articles'])

    @app.route("/technology", methods=['GET', 'POST'])
    def technology():
        if request.method == 'POST':
            title = request.form['search']
            if not title:
                return
            else:
                return redirect(url_for('search',query=title))
        data = getHeadlines('technology')
        if data['status'] == 'error':
            return render_template('error.html', error_message="Too many requests! API is on a cooldown. Come back later.")
        else:
            return render_template('technology.html', articles=data['articles'])
    
    @app.route("/sports", methods=['GET', 'POST'])
    def sports():
        if request.method == 'POST':
            title = request.form['search']
            if not title:
                return
            else:
                return redirect(url_for('search',query=title))
        data = getHeadlines('sports')
        if data['status'] == 'error':
            return render_template('error.html', error_message="Too many requests! API is on a cooldown. Come back later.")
        else:
            return render_template('sports.html', articles=data['articles'])

    @app.route("/entertainment", methods=['GET', 'POST'])
    def entertainment():
        if request.method == 'POST':
            title = request.form['search']
            if not title:
                return
            else:
                return redirect(url_for('search',query=title))
        data = getHeadlines('entertainment')
        if data['status'] == 'error':
            return render_template('error.html', error_message="Too many requests! API is on a cooldown. Come back later.")
        else:
            return render_template('entertainment.html', articles=data['articles'])
    
    @app.route("/search/<string:query>")
    def search(query):
        data = searchArticles(query)['articles']

        if not data:
            return render_template('error.html', error_message="Couldn't find anything related to: \"{}\"".format(query))
        else:
            return render_template('search.html', articles=data, query=query)
    return app 