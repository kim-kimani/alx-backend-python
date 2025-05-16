import mysql.connector
import pandas as pd
import uuid
from mysql.connector import Error


def connect_db():
    """Connects to the MySQL server"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        print("Connected to MySQL server")
        return connection
    except Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    """Creates the ALX_prodev database if it doesn't exist"""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists")
    except Error as err:
        print(f"Error creating database: {err}")


def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ALX_prodev'
        )
        print("Connected to ALX_prodev database")
        return connection
    except Error as err:
        print(f"Error connecting to database: {err}")
        return None


def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(10, 2) NOT NULL
        )
        """)
        print("Table user_data created successfully")
    except Error as err:
        print(f"Error creating table: {err}")


def insert_data(connection, csv_file):
    try:
        df = pd.read_csv(csv_file)
        df = df.drop_duplicates()

        if 'user_id' not in df.columns:
            df['user_id'] = [str(uuid.uuid4()) for _ in range(len(df))]

        cursor = connection.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE name=name
            """, (row['user_id'], row['name'], row['email'], row['age']))
        connection.commit()
        print("Data inserted successfully")
    except Error as err:
        print(f"Error inserting data: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def stream_users(connection):
    """
    Generator that streams users one by one from the user_data table
    """
    try:
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT * FROM user_data")

        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row

        cursor.close()
    except Error as err:
        print(f"Error streaming data: {err}")