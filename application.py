#from flask_bootstrap import Bootstrap
from flask import Flask, render_template
import datetime

app = Flask(__name__, subdomain_matching=True)
#bootstrap = Bootstrap(app)

@app.route("/")
def index():
    today = datetime.datetime.now()
    isMyBirthday = (today.month == 7 and today.day == 5)
    headline = "Is it Ben's birthday?"
    return render_template("index.html", headline=headline,
     isMyBirthday=isMyBirthday)

@app.route("/", subdomain="when")
def when():
    return render_template("when.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
