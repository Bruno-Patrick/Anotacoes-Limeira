from bcolors import bcolors

class Arquivo:
    def __init__(self):
        pass

    def write(self):
        print(bcolors.WARNING + "\nCaso o arquivo não exista, ele será criado automaticamente!\n" + bcolors.RESET)
        name = str(input("Qual nome do arquivo em que desejas escrever?\nNome do arquivo: "))
        with open(f'Atividade sobre manipulação de arquivos/REFAZENDO/txt/{name}.txt', 'a') as name:
            text = str(input("Digite o texto: "))
            name.write(text)

    def charactersDescribe(self):
        print(bcolors.WARNING + '\n não é necessário informar a extesão do arquivo (.txt)\n' + bcolors.RESET)
        archive = str(input("Qual nome do arquivo em que desejas descreve os caracteres?\nNome do arquivo: "))
        try:
            with open(f'Atividade sobre manipulação de arquivos/REFAZENDO/txt/{archive}.txt', 'r') as archive:
                readlines = archive.readlines()
                charactersCount, vogaisCount, consoantesCount = 0, 0, 0
                for lines in readlines:
                    linessplit = lines.split()

                    for words in linessplit:
                        wordssplit = words.split()

                        for characters in wordssplit:
                           characterslist = list(characters)
                           charactersCount += len(characterslist)
                           consoantesCount += self.consoantes(characterslist)
                           vogaisCount += self.vogais(characterslist)
            print("--------------------------------------------------------")
            print(f"|TOTAL DE LINHAS: {len(readlines)}\n|")
            print(f"|TOTAL DE CARACTERES: {charactersCount}\n|")
            print(f"|TOTAL DE VOGAIS: {vogaisCount}\n|")
            print(f"|TOTAL DE CONSOANTES: {consoantesCount}\n|")
            print(f"|TOTAL DE CARACTERES ESPECIAIS: {charactersCount - consoantesCount - vogaisCount}")
            print("--------------------------------------------------------")
                           
        except FileNotFoundError:
            print(bcolors.FAIL + f'Arquivo não existe! Crie-o primeiro' + bcolors.RESET)

    def consoantes(self, array):
        consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                      'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B',
                      'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
                       'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        count = 0
        for letter in array:
            for consoante in consoantes:
                if letter == consoante:
                    count += 1
        return count
    
    def vogais(self, array):
        vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count = 0
        for letter in array:
            for vogal in vogais:
                if letter == vogal:
                    count += 1
        return count


    def equalarchive(self):
        print(bcolors.WARNING + '\n não é necessário informar a extesão do arquivo (.txt)\n' + bcolors.RESET)
        A1 = str(input("Qual nome do primeiro arquivo que desejas comparar?\nNome do arquivo: "))
        A2 = str(input("Qual nome do segundo arquivo que desejas comparar?\nNome do arquivo: "))
        with open(f'Atividade sobre manipulação de arquivos/REFAZENDO/txt/{A1}.txt') as A1:
            A1reader = A1.read()
            with open(f'Atividade sobre manipulação de arquivos/REFAZENDO/txt/{A2}.txt') as A2:
                A2reader = A2.read()
                if (A1reader == A2reader):
                    return print("Arquivos indênticos")
                return print("Arquivos diferentes")


ar = Arquivo()
ar.equalarchive()