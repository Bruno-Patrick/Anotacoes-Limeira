import sqlite3 as db
from sqlite3 import Error
import os, platform
from typing import List
from Aluno import Aluno
from Disciplinas import Disciplinas
from Notas import Notas
from Responsavel import Responsavel
from Professor import Professor

class Connection:

    def create_connection(self):
        OS = platform.system()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            if not 'Windows' in OS:
                conn = db.connect(f"{dir_path}/alunos.db")
            else:
                conn = db.connect(f"{dir_path}\alunos.db")
        except Error as err:
            raise Exception(err)
        return conn

    def operation(self, query):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

    def inserir(self, object):
        name = type(object).__name__
        query = f"INSERT INTO {name.lower()}({','.join([x[1::] for x in object.__slots__])}) VALUES ("
        valores = []
        for slot in object.__slots__:
            attribute = object.__getattribute__(slot)
            if isinstance(attribute, List):
                lista = []
                if len(attribute) == 0:
                    valores.append("NULL")
                else:
                    for i in attribute:
                        lista.append(i)
                    valor = ','.join(lista)
                    valores.append(valor)
            else:
                valores.append(attribute)
        values = "'"
        values += "','".join(valores)
        values += "'"
        query += f"{values});"
        print(query)
        #self.operation(query)

alunos = """CREATE TABLE IF NOT EXISTS 
    aluno(id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(60) NOT NULL,
    matricula INTEGER NOT NULL UNIQUE, 
    telefone VARCHAR(15),
    email VARCHAR(60), 
    disciplinas INTEGER, 
    responsavel INTEGER,
    notas INTEGER,
    FOREIGN KEY(disciplinas) REFERENCES disciplinas(id),
    FOREIGN KEY(responsavel) REFERENCES responsavel(id),
    FOREIGN KEY(notas) REFERENCES notas(id))"""

responsavel = """CREATE TABLE IF NOT EXISTS
    responsavel(id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(60) NOT NULL,
    telefone VARCHAR(15),
    email VARCHAR(60))
    """

notas = """CREATE TABLE IF NOT EXISTS 
    notas(id INTEGER PRIMARY KEY AUTOINCREMENT, 
    disciplina INTEGER NOT NULL,
    aluno INTEGER NOT NULL,
    nota FLOAT(3,2) NOT NULL,
    FOREIGN KEY(disciplina) REFERENCES disciplinas(id),
    FOREIGN KEY(aluno) REFERENCES alunos(id)
    )"""

disciplinas = """CREATE TABLE IF NOT EXISTS
    disciplinas(id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(60) NOT NULL,
    ano DATE NOT NULL,
    semestre INTEGER NOT NULL,
    professor INTEGER NOT NULL,
    FOREIGN KEY(professor) REFERENCES professor(id))
    """

professor = """
    CREATE TABLE IF NOT EXISTS professor(id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(60) NOT NULL,
    disciplinas INTEGER,
    FOREIGN KEY(disciplinas) REFERENCES disciplinas(id))
    """

usuario = """CREATE TABLE IF NOT EXISTS
    usuario(id INTEGER PRIMARY KEY AUTOINCREMENT,
    hash VARCHAR(254) NOT NULL,
    username VARCHAR(45),
    professor INTEGER NOT NULL,
    FOREIGN KEY(professor) REFERENCES professor(id))
    """

dd = Connection()
dd.operation(alunos)
dd.operation(responsavel)
dd.operation(notas)
dd.operation(disciplinas)
dd.operation(professor)
dd.operation(usuario)
prof = Professor("Bruno")
#dis = Disciplinas("TESI1",2022,"Limeira","CCET20",2)
#prof.add_disciplina(dis)
res = Responsavel("Bruno","(68)999010276","021996.bmx@gmail.com")
dd.inserir(prof)
dd.inserir(res)