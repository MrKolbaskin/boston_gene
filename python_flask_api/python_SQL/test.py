import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

#Создание таблицы
create_table = 'CREATE TABLE users (id int, username text, password text)'
cursor.execute(create_table)

#Добавление строки в таблицу
user = (1, 'jose', 'asdf')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user)

#добавление нескольких строк
users = [
	(2, 'rolf', 'asdf'),
	(3, 'anne', 'xyz')
]
cursor.executemany(insert_query, users)

#Выбор строк в таблице
select_query = 'SELECT * FROM users'
for row in cursor.execute(select_query):
	print(row)

connection.commit()

connection.close()