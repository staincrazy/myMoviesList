from flask import Flask, render_template, request
import sqlite3


def createDatabase():
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Score INT)''')
    connection.commit()
    connection.close()


def drop_database():
    connection = sqlite3.connect("movies.db")
    connection.cursor().execute('''DELETE * FROM TABLE Movies''')


def connect_to_db():
    connection = sqlite3.connect("movies.db")
    connection.row_factory = sqlite3.Row
    return connection


app = Flask(__name__)


@app.route("/home_page.html", methods=['GET', 'POST'])
def main():
    return render_template("home_page.html")


@app.route("/all_records_page.html")
def tables():
    conn = connect_to_db()
    movies = conn.execute('SELECT * FROM Movies').fetchall()
    conn.close()
    return render_template("all_records_page.html", movies=movies)


@app.route("/add_record_page.html", methods=["GET"])
def records():
    return render_template("add_record_page.html")


@app.route("/add_record_page.html", methods=["POST"])
def addRecord():
    title = request.form["title"]
    director = request.form["director"]
    score = request.form["score"]

    conn = connect_to_db()
    try:
        cur = conn.cursor()
        sqlite3_insert_query = """INSERT INTO MOVIES (Title,Director,Score) VALUES (?,?,?)"""
        data_tuple = (title, director, score)
        cur.execute(sqlite3_insert_query, data_tuple)
        conn.commit()

    except:
        conn.rollback()

    finally:
        conn.close()
        return render_template("add_record_page.html")


@app.route("/all_records_page.html", methods=['POST'])
def deleteRecords():

    if request.form.get('delete_button') == 'Delete All':

        conn = connect_to_db()
        conn.cursor().execute('''DELETE FROM Movies''')
        conn.commit()
        conn.close()

        return render_template("all_records_page.html")

if __name__ == '__main__':
    conn = connect_to_db()
    conn.cursor().execute('''DELETE FROM Movies''')
    conn.commit()
    conn.close()