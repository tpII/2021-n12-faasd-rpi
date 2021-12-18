import sqlite3
import sys
import json
from flask import g

def conexion():
    if "db_conn" not in g:
        g.db_conn = sqlite3.connect('database.db') # Conectar con la bd
    return g.db_conn

def close(e=None):
    conn = g.pop("db_conn", None)

    if conn is not None:
        conn.close()

def add_temp (temp):    # Agregar valor de temperatura a la bd
    conn= conexion()
    curs=conn.cursor()
    curs.execute("INSERT INTO temperatura values(datetime('now'), (?))", (temp,))
    conn.commit()

def add_hum (hum):      # Agregar valor de humedad a la bd
    conn= conexion()
    curs=conn.cursor()
    curs.execute("INSERT INTO humedad values(datetime('now'), (?))", (hum,))
    conn.commit()

def valoresHistoricos(variable):     # Retornar cada 10 valores
    conn= conexion()
    curs= conn.cursor()
    sql= f'''SELECT t.valor, t.timestamp
            FROM
            (
                SELECT valor, timestamp, ROW_NUMBER() OVER (ORDER BY timestamp DESC) AS rownum
                FROM {variable}
            ) AS t
            WHERE t.rownum % 10 = 0
            LIMIT 10'''
    lista= curs.execute(sql).fetchall() # Lista de los ultimos 10 valores de la bd con un paso de 2

    row_headers=[x[0] for x in curs.description] # Extraer encabezados de filas
    lista_json=[]
    for result in lista:  # Recorrer la lista de temperaturas o humedades y convertirlas a JSON
        diccionario= dict(zip(row_headers,[result[0],result[1][5:]])) # ['valor','timestamp'] == row_headers
        lista_json.append((diccionario))  
    
    return lista_json

def init_app(app):
    app.teardown_appcontext(close)