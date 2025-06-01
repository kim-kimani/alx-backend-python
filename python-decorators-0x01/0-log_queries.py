import sqlite3
import functools

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract query from args or kwargs
        if 'query' in kwargs:
            sql_query = kwargs['query']
        elif len(args) > 0:
            sql_query = args[0]
        else:
            sql_query = "Unknown query"

        print(f"Executing SQL Query: {sql_query}")
        return func(*args, **kwargs)
    
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")