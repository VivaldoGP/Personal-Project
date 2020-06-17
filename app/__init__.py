from flask import Flask
from flask_bootstrap import Bootstrap

#instancias
app = Flask(__name__)
bootstrap = Bootstrap()

from .views import page 


def create_app(config):
    app.config.from_object(config)

    bootstrap.init_app(app) #para que el server pueda usar Bootstrap

    app.register_blueprint(page)
    return app