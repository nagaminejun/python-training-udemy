import sqlite3

conn = sqlite3.connect(':memory')

# conn = sqlite3.connect('test_sqlite.db')

curs = conn.cursor()
curs.execute('CREATE TABLE PERSONS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME STRING)')
conn.commit()

# curs.execute('insert into persons(name) values("Mike")')
# conn.commit()

# curs.execute('insert into persons(name) values("Jjj")')
# curs.execute('insert into persons(name) values("Nancy")')
# conn.commit()

# curs.execute('update persons set name = "Michel" where name = "Mike"')

print(curs.fetchall())
# conn.commit()

curs.close()
conn.close()
