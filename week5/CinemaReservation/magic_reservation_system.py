import sqlite3


class MovieCLI:

    def __init__(self):
        self.db = sqlite3.connect('movies.db')
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.cursor.execute('''PRAGMA foreign_keys = ON''')

    def show_movies(self):
        movie_represent = "Current movies:\n"
        movies = self.cursor.execute('''SELECT id, name, rating FROM movies ORDER BY rating DESC''')
        for row in movies:
            movie_represent += "[{id}] - {name} - ({rating})\n".format(**row)

        return movie_represent

    def show_movie_projections(self, movie_id, projection_date=""):
        movie_projections = ""
        if projection_date == "":
            movies = self.cursor.execute('''SELECT * FROM projections
                                        INNER JOIN movies
                                        ON projections.movie_id = movies.id
                                        WHERE movie_id = ?
                                        ORDER BY projection_date || time''',
                                        (movie_id,))
            projections_str = "[{id}] - {projection_date} {time} ({type})\n"
        else:
            movies = self.cursor.execute('''SELECT * FROM projections
                                        INNER JOIN movies
                                        ON projections.movie_id = movies.id
                                        WHERE movie_id = ?
                                        AND projection_date = ?
                                        ORDER BY projection_date || time''',
                                        (movie_id, projection_date))
            projections_str = "[{id}] - {time} ({type})\n"

        for row in movies:
            if row["name"] not in movie_projections:
                message = "Projections for movie '{}':\n"
                movie_projections += message.format(row["name"])

            movie_projections += projections_str.format(**row)

        return movie_projections

    def make_reservation(self, username, projection_id, row, col):
        info_to_insert = (username, projection_id, row, col)
        self.cursor.execute('''INSERT INTO reservations(username, projection_id, row, col),
                                VALUES=(?, ?, ?, ?)''', info_to_insert)

    def take_available_spots(self, projections):
        projection_ids = ()
        ids = []
        projections.pop(0)
        for projection in projections:
            projection_ids += (int(projection[1]), )

        projection_id = self.cursor.execute('''SELECT max(id) FROM reservations
                                            WHERE movie_id IN ?''',
                                            projection_ids)

        for row in projection_id:
            ids.append(row["id"])

        return ids

    def make_reservation_interface(self):
        username = input("Step 1 (User): Choose name> ")
        number_tickets = int(input("Step 2 (User): Choose number of tickets> "))
        print(self.show_movies())
        number_movie = int(input("Step 2 (Movie): Choose a movie> "))
        projections = self.show_movie_projections(number_movie)
        projections = projections.split("\n")
        projections.pop(0)
        #ids = self.take_available_spots(projections)
        print(projections)
        # for index, projection_id in enumerate(ids):
        #     available_spots = str(100 - projection_id)
        #     available_str = " - {} spots available"
        #     projections[index] += available_str.format(available_spots)

        #print("\n".join(projections))

    def get_input(self):
        command = input("Enter command> ")
        command = command.split(" ")
        return command

    def interface(self):
        command = self.get_input()
        while command[0] != "exit":
            if command[0] == "show_movies":
                print(self.show_movies())
                command = self.get_input()
            elif command[0] == "show_movie_projections":
                movie_id = int(command[1])
                if len(command[2]) > 0:
                    projection_date = command[2]
                else:
                    projection_date = ""

                print(self.show_movie_projections(movie_id, projection_date))
                command = self.get_input()
            elif command[0] == "make_reservation":
                #TODO
                self.make_reservation_interface()
            else:
                print("Bad input!")
                command = self.get_input()
        else:
            print("Goodbye!")


def main():
    cinema = MovieCLI()
    cinema.interface()
    #print(cinema.show_movies())
    #print(cinema.show_movie_projections(2, "2014-04-02"))
    #print(cinema.show_movie_projections(1))

if __name__ == '__main__':
    main()
