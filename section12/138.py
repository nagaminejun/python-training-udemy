import mysql.connector


# conn = mysql.connector.connect(host='127.0.0.1')
# cursor = conn.cursor()
# cursor.execute(
#     'create database test_mysql_database'
# )
# cursor.close()
# conn.close()

conn = mysql.connector.connect(host='127.0.0.1', database='test_mysql_database')
cursor = conn.cursor()
# cursor.execute(
#     'create table persons(id int not null auto_increment, name varchar(14) not null, primary key(id))'
# )

cursor.execute('insert into persons(name) values("Mike")')

conn.commit()
cursor.close()
conn.close()
