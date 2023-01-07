from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/greet/<name>/')
def greet_name(name: str):
    return f'Hello {name}!'
