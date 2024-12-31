import sqlite3

def get_db_connection():

    conn = sqlite3.connect('movies.db')
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Score INT)''')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_movies():

    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()
    return movies

def add_record(title, director, score):

    if None in (title, director, score):
        return False

    conn = get_db_connection()
    cursor = conn.cursor()

    insert_query = """INSERT INTO MOVIES (Title,Director,Score) VALUES (?,?,?)"""
    movie_data_tuple = (title, director, score)

    try:
        cursor.execute(insert_query, movie_data_tuple)
        conn.commit()

    except Exception:
        conn.rollback()
        return False

    finally:
        conn.close()

    return True


def delete_all_movies():
    conn = get_db_connection()
    conn.execute('DELETE FROM movies')
    conn.commit()
    conn.close()

def get_specific_data():
    pass