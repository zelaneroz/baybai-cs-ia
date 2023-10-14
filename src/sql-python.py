import sqlite3

connection = sqlite3.connect("spentio.db")

#step 2 - get the cursor to the database
cursor = connection.cursor()

#step 3 - ready to add sql commands
query = f"""CREATE TABLE if not exists users(
    id integer primary key,
    email text not null unique,
    password text not null,
    username text not null
)"""

cursor.execute(query)
connection.commit()
connection.close()