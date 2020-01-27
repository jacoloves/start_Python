import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE book (title VARCHAR(100),
author VARCHAR(100), year INT)''')

conn.commit()

curs.close()