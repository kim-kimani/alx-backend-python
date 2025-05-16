# 🐍 Python Generators - Task 0: Stream Rows from SQL Database

This project demonstrates how to use **Python generators** to stream data from a CSV file and insert it into a MySQL database.

The script creates a database, a table, and inserts data using a generator to efficiently stream data without loading the entire file into memory.

---

## 🎯 Objective

To create a Python script that:
- Sets up a MySQL database and table
- Streams data from a CSV file using a generator
- Inserts the data into the database row by row

---

## 🧰 Requirements

- Python 3.x
- MySQL Server running locally
- mysql-connector-python library (`pip install mysql-connector-python`)
- A CSV file named `user_data.csv` with the following format:

```csv
name,email,age
John Doe,john@example.com,30
Jane Smith,jane.smith@email.com,25
...