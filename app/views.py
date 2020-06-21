#class
from flask import Blueprint #class
#functions
from flask import render_template, request 
from .geodesy import grav_normal
from .forms import InputForm

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


@page.route('/grav', methods = ['GET', 'POST'])
def geodesy():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = grav_normal(form.lat.data)
    else:
        result = None
    return render_template('grav.html', title = 'gravity',
    form=form, result=result)