from flask import *

app = Flask(__name__)


@app.route("/")
@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title)
