import sqlite3

conn = sqlite3.connect("sortify.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT,
    path TEXT,
    content TEXT,
    label TEXT,
    confidence REAL
)
""")

conn.commit()


def insert_document(name, path, content, label, confidence):

    print("\n===================================")
    print("       DATABASE OPERATION")
    print("===================================\n")

    cursor.execute(
        """
        INSERT INTO documents
        (file_name, path, content, label, confidence)
        VALUES (?, ?, ?, ?, ?)
        """,
        (name, path, content, label, confidence)
    )

    conn.commit()
    print("Data Inserted Successfully")
    print("File Name :", name)
    print("Category :", label)