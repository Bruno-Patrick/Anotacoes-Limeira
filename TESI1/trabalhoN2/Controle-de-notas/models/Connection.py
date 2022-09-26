import sqlite3 as db
from sqlite3 import Error
import os

class Connection:

    def create_connection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            conn = db.connect(f"/home/bruno.patrick/Downloads/Anotacoes-Limeira-main/TESI1/trabalhoN2/Controle-de-notas/models/alunos.db")
        except Error as err:
            raise Exception(err)
        return conn

    def operation(self, query):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

aluno = """CREATE TABLE IF NOT EXISTS 
    aluno(id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(60) NOT NULL,
    matricula INTEGER NOT NULL UNIQUE, 
    telefone VARCHAR(15),
    email VARCHAR(60), 
    disciplinas BIGINT(20), 
    responsavel BIGINT(20),
    notas BIGINT(20),
    FOREIGN KEY(disciplinas) REFERENCES disciplinas(id),
    FOREIGN KEY(responsavel) REFERENCES responsavel(id),
    FOREIGN KEY(notas) REFERENCES notas(id))"""

notas = """CREATE TABLE IF NOT EXISTS 
    notas(id INTEGER PRIMARY KEY AUTOINCREMENT, 
    disciplina BIGINT(20) NOT NULL,
    aluno BIGINT(20) NOT NULL,
    nota FLOAT(3,2) NOT NULL,
    FOREIGN KEY(disciplina) REFERENCES disciplinas(id),
    FOREIGN KEY(aluno) REFERENCES alunos(id)
    )"""

disciplinas = """CREATE TABLE IF NOT EXISTS
    disciplinas(id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(60) NOT NULL,
    ano DATE,
    semestre INTEGER,
    professor BIGINT(20))
"""

dd = Connection()
dd.operation(aluno)