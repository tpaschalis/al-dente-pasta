import datetime
import os
import sqlite3

from flask import Flask, redirect
from flask import g

app = Flask(__name__)

## 
##  http://flask.pocoo.org/docs/1.0/patterns/sqlite3/ 
##  Test how connection between flask and sqlite3 works.
##
##   I have created a table using
## CREATE TABLE connections(datetime text)
##
##   We' will try to insert a new record with a datetime string
## every we GET the /add route 
##
##   Also, we'll get back the entirety of the table using a simple
## SELECT * FROM connections when we GET the /list route
##



# A connection is created whenever an application context/request is created
# The database connection is terminated when the context is destroyed
DATABASE = 'demo.db'

def get_db():
        db = getattr(g, '_database', None)
        if db is None :
            db = g._database = sqlite3.connect(DATABASE)
        return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
            db.close()



# Simple definitions of routes
@app.route('/')
def index():
    return """Available Routes : <br>
    / <br>
    /hello <br>
    /add <br>
    /list <br> <br>

    Demo to execute database query using GET request"""

@app.route('/hello')
def hello_world():
        return "Hello, peeps!"


# Check how the database connection is used with the get_db()
# It's easy as pie to execute queries. We're always using placeholders.
@app.route('/add')
def add_record():
    conn = get_db()
    c = conn.cursor()

    clock = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    res = (clock, )
    
    print("Inserting ", res, "into database...")
    c.execute(""" INSERT INTO connections VALUES(?) """, res)
    conn.commit()
    return redirect('/')

# Using a couple of helpful functions for easier parsing of query results,
# each query result is returned as a tuple
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/list')
def show_records():
    res = "<br>"
    for entry in query_db(""" SELECT * FROM connections """):
        print(entry)
        res = res + str(entry) + "<br>"
    return res

# Initialization stuff
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
