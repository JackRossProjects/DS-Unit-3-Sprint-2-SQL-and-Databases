import pymongo
import json
import sqlite3

'''
client = pymongo.MongoClient("mongodb+srv://USER:PASS@CLUSTER.mongodb.net/test?retryWrites=true&w=majority")
db = client.rpg

# get the the data from rpg.json into a dictionary
rpg_file = open('/home/jack/Desktop/rpg.json')
rpg_str = rpg_file.read()
rpg_data = json.loads(rpg_str)[0:]

# insert the json data into the database
db.rpg.insert_many(rpg_data)

print(list(db.rpg.find()))

'''


# OR




# Make a connection
conn = sqlite3.connect('/home/jack/Downloads/rpg_db.sqlite3')


# Create a cursor
char_curs = conn.cursor()

# Get the whole table
query = '''SELECT * FROM charactercreator_character'''
data = char_curs.execute(query).fetchall()


# Using 3.4 connection string
client = pymongo.MongoClient("mongodb+srv://USER:PASS@CLUSTER.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


for row in data:
    # Create the character doc for each row
    char_doc = {
        'id':row[0],
        'name':row[1],
        'level':row[2],
        'exp':row[3],
        'hp':row[4],
        'strength':row[5],
        'intelligence':row[6],
        'dexterity':row[7],
        'wisdom':row[8]
    }
    db.test.insert_one(char_doc)

print(list(db.test.find()))

'''
I still find it easier to use relational databases as opposed to MongoDB.
Data retrieval seems more complicated in Mongo but it seems like I'll be
able to do cooler things with it in the long run. I think I like relational
systems better right now because I'm very confident with SQL.
'''
