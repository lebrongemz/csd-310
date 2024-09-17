import mysql.connector

db_config = {
    'user': 'root',
    'password': 'Deadisland@2',
    'host': 'localhost',
    'database': 'movies'
}

def connect_to_db(config):
    try:
        connection = mysql.connector.connect(**config)
        print("Successfully connected to the database.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def execute_query(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def main():
    connection = connect_to_db(db_config)
    if connection:
        cursor = connection.cursor()
        studio_query = "SELECT * FROM studio;"
        studios = execute_query(cursor, studio_query)
        print("Studios Table:")
        for row in studios:
            print(row)
        genre_query = "SELECT * FROM genre;"
        genres = execute_query(cursor, genre_query)
        print("\nGenres Table:")
        for row in genres:
            print(row)
        short_movies_query = "SELECT name FROM movies WHERE run_time < 120;"
        short_movies = execute_query(cursor, short_movies_query)
        print("\nMovies with Runtime Less Than 2 Hours:")
        for row in short_movies:
            print(row[0])
        director_query = "SELECT director, GROUP_CONCAT(name) FROM movies GROUP BY director;"
        directors = execute_query(cursor, director_query)
        print("\nFilms Grouped by Director:")
        for row in directors:
            print(f"Director: {row[0]}, Films: {row[1]}")
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    main()
