# In terminal we did - export FLASK_APP = app.py
# -> flask run
# refresh fails till the time we don't have endpoints defined
# /endpoint/ way of declaring is better to /endpoint as this allows only access through / included.
# wasn't working due to templates folder not being there - as per Jinja2

import datetime
import os
from flask import Flask, render_template, request
from pymongo import MongoClient
#from dotenv import load_dotenv

#load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://gaganchaudhary74:cA0hCXcewnGAeWXQ@code-test-ground.mzeyb3b.mongodb.net/Microblog")
    app.db = client.Microblog

#entries = [] # later to be replaced with mongo db database -> intial POC

    @app.route("/", methods = ["GET","POST"])
    def home():
        #print([e for e in app.db.Entries.find({})])
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            #entries.append((entry_content,formatted_date))
            app.db.Entries.insert_one({"content":entry_content,"date":formatted_date})

        entries_with_date = [(
            entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"],'%Y-%m-%d').strftime("%b %d")
            )
            for entry in app.db.Entries.find({})
        ]
        return render_template("home.html",entries=entries_with_date)

    return app