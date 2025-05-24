# 📚 Monthly Work Log — May 2025  

> This is my monthly summary of what I worked on, learned, and achieved during May 2025 as part of the **ALX Software Engineering Program**.

---

## 🧠 What I Worked On

This month, I focused on mastering **Python decorators**, **context managers**, and **asynchronous programming concepts**. Key topics included:

- Creating custom decorators for logging SQL queries, managing database connections, and caching query results.
- Building reusable context managers to handle database setup and teardown automatically.
- Exploring asynchronous database queries using `aiosqlite` and `asyncio`.

Projects completed:
- [`0-log_queries.py`](python-decorators-0x01/0-log_queries.py)
- [`1-with_db_connection.py`](python-decorators-0x01/1-with_db_connection.py)
- [`2-transactional.py`](python-decorators-0x01/2-transactional.py)
- [`3-retry_on_failure.py`](python-decorators-0x01/3-retry_on_failure.py)
- [`4-cache_query.py`](python-decorators-0x01/4-cache_query.py)
- [`0-databaseconnection.py`](python-context-async-operations-0x02/0-databaseconnection.py)
- [`1-execute.py`](python-context-async-operations-0x02/1-execute.py)
- [`3-concurrent.py`](python-context-async-operations-0x02/3-concurrent.py)

---

## 🏆 My Achievements

- Successfully implemented multiple Python decorators that automate repetitive tasks like logging, connection handling, and transaction management.
- Built two reusable context managers for database operations.
- Gained hands-on experience with asynchronous programming using `asyncio` and `aiosqlite`.
- Completed all required projects in the **Decorators and Context Managers** section of ALX.

---

## 🧩 Learnings from Failures & Challenges

- Learned how to debug decorator order when stacking them (e.g., `@with_db_connection` before `@transactional`).
- Realized the importance of proper exception handling inside decorators and context managers to avoid silent failures.
- Faced challenges setting up `aiosqlite`, but resolved it by installing dependencies correctly and understanding async workflow structure.

---

## 🌟 Monthly Highlights

- First exposure to real-world uses of **decorators** in database applications.
- Mastered the `__enter__` and `__exit__` protocol for building safe and efficient context managers.
- Got comfortable with **asynchronous I/O** and concurrent execution patterns in Python.
- Built a solid foundation for working with more complex backend systems in the future.

---

💬 *“The only way to do great work is to love what you do.” – Steve Jobs*
