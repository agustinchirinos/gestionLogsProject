from flask import Flask, render_template, request
from flask_recaptcha import ReCaptcha

from .log.logs import configure_logging

app = Flask(__name__)
app.config["RECAPTCHA_SITE_KEY"] = "6LfKDigfAAAAAPeyJWQui0S-rpso7cBg8daT7RnC"
app.config["RECAPTCHA_SECRET_KEY"] = "6LfKDigfAAAAAP9omHFwKzNdGBK2asx169vt-Eqq"

recaptcha = ReCaptcha(app)

from .public import public

logger = configure_logging(__name__)

def create_app():
    app.register_blueprint(public)
    return  app