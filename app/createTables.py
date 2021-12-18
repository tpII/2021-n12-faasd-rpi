import sqlite3 as lite
import sys

conn = lite.connect('database.db')

with conn:
    
    cur = conn.cursor() 
    cur.execute("DROP TABLE IF EXISTS temperatura")
    cur.execute("DROP TABLE IF EXISTS humedad")
    cur.execute("CREATE TABLE temperatura(timestamp DATETIME, valor NUMERIC)")
    cur.execute("CREATE TABLE humedad(timestamp DATETIME, valor NUMERIC)")
    