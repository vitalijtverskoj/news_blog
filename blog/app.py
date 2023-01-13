from time import time

from flask import Flask, g, render_template
from flask import request

from blog.article.views import article
from blog.user.views import user


index = Flask(__name__)


@index.route('/')
def hello():
    return render_template('index.html')


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
