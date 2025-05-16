#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error


def stream_users_in_batches(batch_size):
    """
    Generator function that fetches users in batches from the user_data table.
    Yields one batch (a list of rows) at a time.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # Replace with your MySQL username
            password="your_password",  # Replace with your MySQL password
            database="ALX_prodev"
        )

        if connection.is_connected():
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM user_data")

                batch = []
                for row in cursor:
                    batch.append(row)
                    if len(batch) == batch_size:
                        yield batch
                        batch = []

                # Yield any remaining rows in the last batch
                if batch:
                    yield batch

    except Error as err:
        print(f"Database error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def batch_processing(batch_size):
    """
    Processes users in batches. Filters and prints users whose age > 25.
    Uses no more than 3 loops in total.
    """
    for batch in stream_users_in_batches(batch_size):
        # First loop: filter users
        filtered_users = [user for user in batch if user['age'] > 25]

        # Second loop: process and print users
        for user in filtered_users:
            print(user)

        # No third loop needed — filtering and printing done