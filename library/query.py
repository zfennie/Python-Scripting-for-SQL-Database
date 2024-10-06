"""
QUERY
Query the database
"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the table"""
    conn = sqlite3.connect("icu_hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM icu_hospital")
    print("Top 5 rows of the table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
