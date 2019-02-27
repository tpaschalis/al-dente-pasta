import sqlite3

# Read the docs
# https://docs.python.org/3/library/sqlite3.html

# Initialize connection and cursor
conn = sqlite3.connect('demo.db')
c = conn.cursor()


# # Execute commands
# c.execute(""" CREATE TABLE users
#                (name text, surname text, id integer, spent real) """)
# c.execute(""" INSERT INTO users VALUES ('John', 'Doe', 5, 104.4) """)

# # Avoid SQL injection by using placeholder parameters
# group_1 = [('Mary', 'Rose', 6, 97.3),
#         ('Andrew', 'Grimm', 7, 10.3),
#         ('Zooey', 'Towns', 8, 61.9),
#        ]
# c.executemany(""" INSERT INTO users VALUES(?, ?, ?, ?) """, group_1)

foo = (50,)
bar = (6,)
c.execute(""" SELECT * FROM users WHERE spent > ? """, foo)
print("Spent > 50")
print(c.fetchone())

print("Id >= 6")
for row in c.execute(""" SELECT * FROM users WHERE id >= ? """, bar):
    print(row)

# Save changes and close the db
conn.commit()
conn.close()
