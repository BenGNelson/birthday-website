from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    today = datetime.datetime.now()
    isMyBirthday = (today.month == 7 and today.day == 5)
    headline = "Is it Ben's birthday?"
    return render_template("index.html", headline=headline,
     isMyBirthday=isMyBirthday)
