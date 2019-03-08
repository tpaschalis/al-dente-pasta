#-*- coding: utf-8 -*-

import datetime
import time
import os
import sqlite3
from flask import json, request
import uuid

from flask import Flask, redirect
from flask import g

app = Flask(__name__)

DATABASE = 'copypasta.db'

# Database connection, teardown and query
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

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def assert_post(rd):
    return True

# Simple definitions of routes
@app.route('/')
def index():
    return "Hey mom!"

@app.route('/db')
def summary():
    # Return a json response of all available uids
    all_entries = {}
    for e in query_db(""" SELECT * FROM copypastas """):
        all_entries[e[0]] = "http://157.230.231.216:5000/view/"+e[0]
    response = app.response_class(
        response = json.dumps(all_entries),
        status = 200,
        mimetype = 'application/json'
    )
    return response

@app.route('/view/<uId>')
def fetch_paste(uId):
    print(type(uId))
    print(uId)
    entry = {}
    fetched = query_db(""" SELECT uniqueId, isodate, expireType, content FROM copypastas WHERE uniqueId = ? """, (uId,) ) # Substituted variable must be tuple-like
    print(fetched)
    print(len(entry))
    entry['uniqueId']   = fetched[0][0]
    entry['isodate']    = fetched[0][1]
    entry['expireType'] = fetched[0][2]
    entry['content']    = fetched[0][3]

    response = app.response_class(
        response = json.dumps(entry),
        status = 200,
        mimetype = 'application/json'
    )
    return response

@app.route('/new', methods = ['GET', 'POST'])
def submit_new():

    if request.method == 'POST' and request.is_json:
        req_data = request.get_json()
        if not assert_post(req_data):
            return "Malformed Post Data"

        newId = str(uuid.uuid4()).replace('-', '')
        newId = "0" + newId[:6]
        isodate = datetime.datetime.utcnow().replace(microsecond=0).isoformat()
        new_paste = (newId, isodate, req_data['expireType'], req_data['content'],)

        get_db().execute(""" INSERT INTO copypastas (uniqueId, isodate, expireType, content) VALUES (?, ?, ?, ?) """, new_paste)
        get_db().commit()
        time.sleep(0.5)

        return redirect('http://157.230.231.216:5000/view/' + newId)

    if request.method == 'GET':
        return 'Submit a new paste, like \n\n `curl --header "Content-Type: application/json"   --request POST   --data \'{"content":"Once Upon a Time in Talahassee","expireType":"y"}\'   http://localhost:5000/new` '

    return "Malformed Request, something went wrong"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
