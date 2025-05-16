#!/usr/bin/env python3
import seed


def paginate_users(page_size, offset):
    """
    Fetches a page of users from the database.
    Returns a list of users for that page.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """
    Generator function that yields pages of user data lazily.
    Loads the next page only when needed.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:  # No more data
            break
        yield page
        offset += page_size