import sqlite3
db = sqlite3.connect('books.db')

sql = 'select * from book order by year'
for row in db.execute(sql):
    print(row)