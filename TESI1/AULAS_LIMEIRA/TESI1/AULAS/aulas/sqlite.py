import sqlite3
from sqlite3 import Error

def connection_db():
    conn = None
    try:
        conn = sqlite3.connect("/home/bruno.patrick/Área de Trabalho/AULAS_LIMEIRA/TESI1/aulas/aula.db")
    except Error as e:
        print(e)
    return conn    

def createTable(query):
    conn = connection_db()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        return print('Successful operation') 
    except Error as e:
        return print(e)


def operation(query):
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        return print('Successful operation')
    except Error as e:
        return print(e)

def consult(query):
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
    except Error as e:
        print(e)
        
#insertQuery = "INSERT INTO cliente(nome, cpf) VALUES ('Bruno Patrick','031556'), ('Bruno Patrick','1234515');"
deleteQuery = "DELETE FROM cliente WHERE id = 5;"
updateQuery = "UPDATE cliente SET nome='cuin' WHERE id = 3;"
selectQuery = "SELECT * FROM cliente;"
create = "CREATE TABLE IF NOT EXISTS cliente(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(60) NOT NULL, cpf VARCHAR(11) NOT NULL);"

print(consult(selectQuery))