import sqlite3

class DatabaseConnection:
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        # Open/establish a connection to the SQLite database
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the database connection
        if self.connection:
            self.connection.close()


# Using the custom context manager to query the database
with DatabaseConnection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()

# Print the fetched results
print(results)

