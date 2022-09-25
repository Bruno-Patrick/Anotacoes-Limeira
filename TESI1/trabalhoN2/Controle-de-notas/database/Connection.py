import sqlite3 as db
from sqlite3 import Error
import os

def create_connection():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        conn = db.connect(f"{dir_path}/alunos.db")
        return conn
    except Error as err:
        raise Exception(err)

def operation(query):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        conn.commit()
        conn.close()
    except Error as err:
        print(err)