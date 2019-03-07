# -*- coding: utf-8 -*-

import datetime
import sqlite3
import uuid

# Database Connection
conn = sqlite3.connect('copypasta.db')
c = conn.cursor()


# Creation of new values
uniqueId = str(uuid.uuid4()).replace('-', '')
uniqueId = "0" + uniqueId[:6]

isodate = datetime.datetime.utcnow().replace(microsecond=0).isoformat()

expireType = 'y'

#content = """
#"""
content = """
"""

data = (uniqueId, isodate, expireType, content)


# Execute insertion and close connection
c.execute(""" INSERT INTO copypastas(uniqueId, isodate, expireType, content) VALUES (?, ?, ?, ?) """, data)

conn.commit()
conn.close()
