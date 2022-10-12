import sqlite3
from sqlite3 import Error


def connection():
    conn = None
    try:
        conn = sqlite3.connect("/home/bruno.patrick/Área de Trabalho/AULAS_LIMEIRA/TESI1/aulas/aula.db")
    except Error as e:
        print(e)
    return conn

def operation(query):
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        return print('Successful operation')
    except Error as e:
        return print(e)

def consult(query):
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
    except Error as e:
        print(e)