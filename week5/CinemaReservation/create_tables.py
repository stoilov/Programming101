import sqlite3


db = sqlite3.connect('movies.db')
cursor = db.cursor()
cursor.execute('''PRAGMA foreign_keys = ON''')
cursor.execute('''CREATE TABLE IF NOT EXISTS
                  movies(id INTEGER PRIMARY KEY, name TEXT, rating REAL)''')
movies = [
    ("The Hunger Games: Catching Fire", 7.9),
    ("Wreck-It Ralph: Catching Fire", 7.8),
    ("Her", 8.3)
]
cursor.executemany('''INSERT INTO movies(name, rating)
                 VALUES(?, ?)''', movies)
db.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS
                  projections(
                    id INTEGER PRIMARY KEY,
                    movie_id INTEGER,
                    type TEXT,
                    projection_date TEXT,
                    time TEXT,
                    FOREIGN KEY(movie_id) REFERENCES movies(id))''')
projections = [
    (1, "3D", "2014-04-01", "19:10"),
    (1, "2D", "2014-04-01", "19:00"),
    (1, "4DX", "2014-04-02", "21:00"),
    (3, "2D", "2014-04-05", "20:20"),
    (2, "3D", "2014-04-02", "22:00"),
    (2, "2D", "2014-04-02", "19:30")
]
cursor.executemany('''INSERT INTO projections(movie_id, type, projection_date, time)
                 VALUES(?, ?, ?, ?)''', projections)
db.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS
                  reservations(id INTEGER PRIMARY KEY,
                    username TEXT,
                    projection_id INTEGER,
                    row INTEGER,
                    col INTEGER,
                    FOREIGN KEY(projection_id) REFERENCES projections(id))
                  ''')
db.commit()
db.close()
