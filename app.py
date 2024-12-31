from operator import methodcaller

from flask import Flask, render_template, request
from flask import jsonify
from dao import *

app = Flask(__name__)

# GET METHODS

@app.route("/home_page.html", methods=['GET', 'POST'])
def main():
    return render_template("home_page.html")

@app.route("/all_records_page.html",methods=['GET'])
def tables():
    movies = fetch_all_movies()
    return render_template("all_records_page.html", movies=movies)

@app.route("/add_record_page.html", methods=["GET"])
def records():
    return render_template("add_record_page.html")

# POST METHODS

@app.route("/add_record_page", methods=["POST"])
def addRecord():

    title = request.form["title"]
    director = request.form["director"]
    score = request.form["score"]

    is_added = add_record(title,director, score)

    return jsonify({"success":is_added, "message": "The movie is added"})


@app.route("/delete_all", methods=['POST'])
def deleteRecords():
    delete_all_movies()
    return render_template("all_records_page.html")

