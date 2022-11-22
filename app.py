from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home.html", methods=['GET', 'POST'])
def main():
    return render_template("home.html")


@app.route("/tables.html")
def tables():
    return render_template("tables.html")


@app.route("/records.html")
def records():
    return render_template("records.html")
