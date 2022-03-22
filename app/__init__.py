from flask import Flask, render_template, request

from .log.logs import configure_logging

app = Flask(__name__)


from .public import public

logger = configure_logging(__name__)

def create_app():
    app.register_blueprint(public)
    return  app