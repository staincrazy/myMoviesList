import sqlite3


def create_database():
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Score INT)''')
    connection.commit()
    connection.close()


def add_movie_to_database(title, director, user_score):
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    sqlite3_insert_query = """INSERT INTO MOVIES (Title,Director,Score) VALUES (?,?,?)"""
    data_tuple = (title, director, user_score)
    cursor.execute(sqlite3_insert_query, data_tuple)

    connection.commit()
    connection.close()


def select_all_from_database():
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Movies''')

    movies = cursor.fetchall()
    for movie in enumerate(movies, start=0):
        print(movie)


def select_specific_data(field, data):
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()

    if field.lower() == 'title':
        cursor.execute(("SELECT * FROM Movies WHERE Title=?"), (data,))
    elif field.lower() == 'director':
        cursor.execute(("SELECT * FROM Movies WHERE Director=?"), (data,))
    elif field.lower() == 'user_score':
        cursor.execute(("SELECT * FROM Movies WHERE Score=?"), (data,))
    else:
        return 'Movie not found'

    movie = cursor.fetchall()
    connection.commit()
    connection.close()
    return movie


if __name__ == '__main__':
    select_all_from_database()
    print(select_specific_data('title', 'Matrix'))
    print(select_specific_data('director', 'Wachovski'))
    print(select_specific_data('user_score', '10'))
