#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error


def stream_user_ages():
    """
    Generator function that yields user ages one by one from the user_data table.
    Uses yield to stream data without loading all records into memory.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # Replace with your MySQL username
            password="your_password",  # Replace with your MySQL password
            database="ALX_prodev"
        )

        if connection.is_connected():
            with connection.cursor() as cursor:
                cursor.execute("SELECT age FROM user_data")

                # Yield one age at a time
                for row in cursor:
                    yield row[0]

    except Error as err:
        print(f"Database error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def calculate_average_age():
    """
    Calculates the average age using the stream_user_ages generator.
    Does not load the entire dataset into memory.
    Uses no more than two loops.
    """
    total_age = 0
    count = 0

    # One loop only
    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        print("No users found.")
        return

    average_age = total_age / count
    print(f"Average age of users: {average_age}")
    return average_age