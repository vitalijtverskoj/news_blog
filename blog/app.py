from time import time

from flask import Flask, g
from flask import request

# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return 'Hello!'
#
#
# @app.route('/greet/<int:name>/')
# def greet_name(name: int):
#     return f'Hello, {isinstance(name, int)}!'
#
#
# @app.route("/user/")
# def read_user():
#     name = request.args.get("name")
#     surname = request.args.get("surname")
#     return f"User {name or '[no name]'} {surname or '[no surname]'}"
#
#
# @app.route("/status/", methods=["GET", "POST"])
# def custom_status_code():
#     if request.method == "GET":
#         return """\
#         To get response with custom status code
#         send request using POST method
#         and pass `code` in JSON body / FormData
#         """
#     print("raw bytes data:", request.data)
#     if request.form and "code" in request.form:
#         return "code from form", request.form["code"]
#     if request.json and "code" in request.json:
#         return "code from json", request.json["code"]
#     return "", 204
#
#
# @app.before_request
# def process_before_request():
#     """
#     Sets start_time to `g` object
#     """
#     g.start_time = time()
#
#
# @app.after_request
# def process_after_request(response):
#     """
#     adds process time in headers
#     """
#     if hasattr(g, "start_time"):
#         response.headers["process-time"] = time() - g.start_time
#     return response
#
#
# @app.errorhandler(404)
# def handler_404(error):
#     app.logger.error(error)
#     return '404'


def create_app() -> Flask:
    app = Flask(__name__)
    return app
