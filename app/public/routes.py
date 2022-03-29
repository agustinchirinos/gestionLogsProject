from flask import render_template, request

import app
from . import public



@public.route('/', methods=["GET","POST"])
def index():  # put application's code here
    app.logger.info("Mensaje de información")
    msg = ""
    if request.method == "POST":
        if app.recaptcha.verify():
            msg = "Eres un humano"
        else:
            msg = "No eres un humano"
    return render_template('index.html', msg=msg)
