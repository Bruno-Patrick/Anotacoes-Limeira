import os
from datetime import date
with open('log001-sex-10-06-2022-11:24.txt', 'w') as escrita:
    cwd = os.getcwd()
    date = date.today()
    escrita.write(f'Current Directoy: {cwd}\n')
    escrita.write(f'Actual Date: {date}\n')

nome_arquivo = input('Nome Arquivo:')
try:
    arquivo = open(nome_arquivo, 'r')
    linhas_lista = arquivo.readlines()
    for dados in linhas_lista:
        print(dados, end='')
    arquivo.close()
except:
    print(f"O arquivo {nome_arquivo}.txt não existe!")