import psycopg2
import sqlite3

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname='ifxqbgfl', user='ifxqbgfl',
                        password='W7SNf_u_VwaJTeuBbFSBDwc2QPB_OjDV', host='drona.db.elephantsql.com')
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query

cur.execute('SELECT * from charactercreator_character;') # UNLESS TESTING, REPLACE CHARCREATOR WITH TEST_TABLE AND DELETE COMMENTS BELOW
### Note - nothing happened yet! We need to actually *fetch* from the cursor
print(cur.fetchall())
'''
# Insert RPG_db data
rpg_conn = sqlite3.connect('/home/jack/Downloads/rpg_db.sqlite3')
rpg_curs = rpg_conn.cursor()

characters = rpg_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

create_character_table = """
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
)
"""

cur.execute(create_character_table)

for character in characters:
  insert_character = """
  INSERT INTO charactercreator_character
  (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
  VALUES """ + str(character[1:])
  cur.execute(insert_character)

conn.commit()

pg_curs = conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = cur.fetchall()

print(characters[0])
print(pg_characters[0])
'''