# In terminal we did - export FLASK_APP = app.py
# -> flask run
# refresh fails till the time we don't have endpoints defined
# /endpoint/ way of declaring is better to /endpoint as this allows only access through / included.
# wasn't working due to templates folder not being there - as per Jinja2

import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

entries = [] # later to be replaced with mongo db database -> intial POC

@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content,formatted_date))
    return render_template("home.html",entries=entries)