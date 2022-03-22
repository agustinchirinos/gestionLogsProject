from flask import Flask, render_template, request



app = Flask(__name__)


from .public import public

def create_app():
    app.register_blueprint(public)
    return  app