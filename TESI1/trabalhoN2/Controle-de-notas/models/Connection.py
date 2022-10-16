from random import random
import sqlite3 as db
from sqlite3 import Error
import os, platform

from Usuario import Usuario
from Aluno import Aluno
from Disciplinas import Disciplinas
from Responsavel import Responsavel
from Professor import Professor

class Connection:

    def create_connection(self):
        OS = platform.system()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            if not 'windows' in OS:
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

    def select(self, query):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        retorno = cursor.fetchall()
        cursor.close()
        return retorno

    def inserir(self, object):
        name = type(object).__name__
        query = f"""INSERT INTO {name.lower()}({','.join([x[1::] for x in object.__slots__ if x != '_id'])}) VALUES ("""
        valores = []
        for slot in object.__slots__:
            if not 'id' in slot:
                attribute = object.__getattribute__(slot)
                valores.append(str(attribute))
        values = '"'
        values += '","'.join(valores)
        values += '"'
        query += f"{values});"
        print(query)
        self.operation(query)

    def getHashByUserName(self, username):
        query = f"SELECT hash FROM usuario WHERE username LIKE '{username}'"
        retorno = self.select(query)
        return retorno
    
    def getUserByUserName(self, username):
        query = f"SELECT * FROM usuario WHERE username like '{username}'"
        retorno = self.select(query)
        return retorno

    def getProfessorByName(self, name):
        query = f"SELECT * FROM professor WHERE nome LIKE '{name}%'"
        retorno = self.select(query)
        return retorno

    def getAllProfessores(self):
        query = f"SELECT * FROM professor"
        retorno = self.select(query)
        return retorno        

    def getConfigurationsByUser(self, userId):
        query = f"SELECT * FROM configurations WHERE usuario = '{userId}'"
        retorno = self.select(query)
        return retorno

    def getDisciplinasbyProfessor(self, professorId, semestre=None, ano=None, codigo=None):
        query = f"""SELECT * FROM disciplinas WHERE 
            `professor` = '{professorId}'
            {"".join([x for x in f"AND `semestre`= '{semestre}'" if semestre])}
            {"".join([x for x in f"AND `ano`= '{ano}'" if ano])}
            {"".join([x for x in f"AND `codigo`= '{codigo}'" if codigo])}"""
        retorno = self.select(query)
        return retorno

    def getAlunoByNome(self, nome: str = ...):
        query = f"SELECT * FROM aluno WHERE nome = '{nome}'"
        retorno = self.select(query)
        return retorno

    def getAlunoDisciplinas(self, alunoID, disciplinaID):
        query = f"SELECT * FROM alunodisciplinas WHERE aluno = '{alunoID}' AND disciplina = '{disciplinaID}'"
        retorno = self.select(query)
        return retorno

    def getAlunosForTvw(self, disciplinaId):
        query = f"""SELECT aluno.id, aluno.nome FROM 
        aluno INNER JOIN alunodisciplinas
        ON aluno.id = aluno AND disciplina = '{disciplinaId}'
        """
        retorno = self.select(query)
        return retorno

    def alterConfigurationsByUser(self, userId, N1Amount, N2Amount):
        query = f"UPDATE configurations SET `atvAmountPartialN1` = '{N1Amount}', `atvAmountPartialN2` = '{N2Amount}' WHERE `usuario` = '{userId}'"
        self.operation(query)

alunos = """CREATE TABLE IF NOT EXISTS 
    aluno(id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(60) NOT NULL,
    matricula INTEGER NOT NULL UNIQUE, 
    telefone VARCHAR(15),
    email VARCHAR(60), 
    responsavel INTEGER,
    FOREIGN KEY(responsavel) REFERENCES responsavel(id))"""

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
    identificador VARCHAR(15) NOT NULL,
    FOREIGN KEY(disciplina) REFERENCES disciplinas(id),
    FOREIGN KEY(aluno) REFERENCES alunos(id)
    )"""

disciplinas = """CREATE TABLE IF NOT EXISTS
    disciplinas(id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(60) NOT NULL,
    ano DATE NOT NULL,
    semestre INTEGER NOT NULL,
    professor INTEGER NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    FOREIGN KEY(professor) REFERENCES professor(id))
    """

professor = """
    CREATE TABLE IF NOT EXISTS 
    professor(id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(60) NOT NULL)    """

usuario = """CREATE TABLE IF NOT EXISTS
    usuario(id INTEGER PRIMARY KEY AUTOINCREMENT,
    hash VARCHAR(254) NOT NULL,
    username VARCHAR(45) UNIQUE,
    professor INTEGER NOT NULL,
    FOREIGN KEY(professor) REFERENCES professor(id))
    """

alunodisciplinas = """
    CREATE TABLE IF NOT EXISTS
    alunodisciplinas(id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno INTEGER NOT NULL,
    disciplina INTEGER NOT NULL,
    FOREIGN KEY(aluno) REFERENCES aluno(id),
    FOREIGN KEY(disciplina) REFERENCES disciplina(id))
    """

configurations = """
    CREATE TABLE IF NOT EXISTS
    configurations(id INTEGER PRIMARY KEY AUTOINCREMENT,
    atvAmountPartialN1 INTEGER,
    atvAmountPartialN2 INTEGER,
    usuario INTEGER NOT NULL,
    FOREIGN KEY(usuario) REFERENCES usuario(id))
    """

dd = Connection()
dd.operation(alunos)
dd.operation(responsavel)
dd.operation(notas)
dd.operation(disciplinas)
dd.operation(professor)
dd.operation(usuario)
dd.operation(alunodisciplinas)
dd.operation(configurations)
prof = Professor("Bruno")

if not dd.getUserByUserName('admin'):
    admin = Usuario('12345','admin','1')
    dd.inserir(admin)

if not dd.getAlunoByNome('bruno'):
    for i in range(0,10):
        matricula = random()
        aluno = Aluno('bruno',matricula)
        dd.inserir(aluno)

brunos = dd.getAlunoByNome('bruno')
for aluno in range(0, 5):
    if not dd.getAlunoDisciplinas(brunos[aluno][0],1):
        dd.operation(F"INSERT INTO alunodisciplinas(aluno,disciplina) VALUES('{brunos[aluno][0]}','1')")

# for i in range(0,5):
#    dd.inserir(prof)
"""
dis = Disciplinas("TESI1",2022,"Limeira","CCET20",2)
res = Responsavel("Bruno","(68)999010276","021996.bmx@gmail.com")
dd.inserir(prof)
dd.inserir(res)
"""