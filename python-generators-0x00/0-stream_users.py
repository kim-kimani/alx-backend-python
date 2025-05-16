#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error


def stream_users():
    """
    Generator function that streams rows one by one from the user_data table.
    Uses yield to return each row as a dictionary.
    """
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # Replace with your MySQL username
            password="your_password",  # Replace with your MySQL password
            database="ALX_prodev"
        )

        if connection.is_connected():
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM user_data")

                # Stream rows one by one using yield
                for row in cursor:
                    yield row

    except Error as err:
        print(f"Database error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()