# Basic Website Template
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About Us")


@app.route("/api/openai")
def prompt():
    return render_template("prompt.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
