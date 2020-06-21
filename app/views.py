from flask import Blueprint #class
from flask import render_template, request #functions

page = Blueprint('page', __name__) #args('context name', 'instance context')

@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html', title = 'Index')

@page.route('/about')
def about():
    return render_template('about.html', title = 'about')

@page.route('/functions')
def functions():
    return render_template('functions.html', title = 'functions')