import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS books (title text, author text, year integer, copies_sold integer)"
cursor.execute(create_table)

connection.commit()
connection.close()