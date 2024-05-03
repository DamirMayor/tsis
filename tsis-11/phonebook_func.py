import sqlite3 as sq


with sq.connect('phonebook.db') as con:
  cur = con.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS phonebook(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT)")

  #1
  
  cur.execute("SELECT * FROM phonebook WHERE name LIKE 'Jo%'")
  print(cur.fetchall())
  cur.execute("SELECT * FROM phonebook WHERE phone LIKE '+7747%'")
  print(cur.fetchall())

  #4

  cur.execute("SELECT * FROM phonebook LIMIT 2, 2 ")
  print(cur.fetchall())

 
