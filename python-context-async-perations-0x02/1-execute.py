import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=None):
        self.query = query
        self.params = params if params is not None else ()
        self.result = None

    def __enter__(self):
        # Establish database connection
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        # Execute the query
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Clean up resources
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


# Using the custom context manager to execute a parameterized query
with ExecuteQuery("SELECT * FROM users WHERE age > ?", (25,)) as query_result:
    print("Users older than 25:")
    for user in query_result.result:
        print(user)