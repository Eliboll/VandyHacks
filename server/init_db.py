import sqlite3

connection = sqlite3.connect('database.db')
FILENAME = "cards.txt"

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (userid, ccid, last_location, phone_number) VALUES (?, ?, ?, ?)",
            (10, "7,3,4", "","6362934121")
            )
cur.execute("INSERT INTO users (userid, ccid, last_location, phone_number) VALUES (?, ?, ?, ?)",
            (7, "9,6,1", "","7327209788")
            )
cur.execute("INSERT INTO users (userid, ccid, last_location, phone_number) VALUES (?, ?, ?, ?)",
            (5, "5,8,9", "","5738237850")
            )
cur.execute("UPDATE users SET last_location = '{}' WHERE userid={}".format("walmart",5))

file = open(FILENAME, "r")
lines = file.readlines()
for line in lines[1:]:
    print(line)
    values = line.split("$")
    cur.execute("INSERT INTO cards (id, specials, categories, base, name, company) VALUES (?, ?, ?, ?, ?, ?)", (values[0],values[3],values[4],values[5],values[1],values[2]))
    row = cur.fetchall()

cur.execute("SELECT * FROM cards")

row = cur.fetchall()
print(row)
connection.commit()
connection.close()