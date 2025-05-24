import sqlite3
import functools

# Global cache to store query results
query_cache = {}

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper


def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Assume 'query' is passed as a keyword argument
        if 'query' in kwargs:
            key = kwargs['query']
        elif len(args) >= 2 and isinstance(args[1], str):
            # If using positional arguments, extract query from args
            key = args[1]
        else:
            return func(*args, **kwargs)  # Can't cache if no query found

        # Check if result is already cached
        if key in query_cache:
            print("Using cached result for query:", key)
            return query_cache[key]

        # Execute function and cache result
        result = func(*args, **kwargs)
        query_cache[key] = result
        print("Cached new result for query:", key)
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#### First call will execute and cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")