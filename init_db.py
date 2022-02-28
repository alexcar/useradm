import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO tbl_user (user_name, user_username, user_password) VALUES (?, ?, ?)",
    ('John Clock', 'john.clock', 'change@123')
)

connection.commit()
connection.close()
