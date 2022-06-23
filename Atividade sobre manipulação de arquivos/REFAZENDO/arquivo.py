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
            print(f"\nTOTAL DE LINHAS: {len(readlines)}")
            print(f"\nTOTAL DE CARACTERES: {charactersCount}")
            print(f"\nTOTAL DE VOGAIS: {vogaisCount}")
            print(f"\nTOTAL DE CONSOANTES: {consoantesCount}")
            print(f"\nTOTAL DE CARACTERES ESPECIAIS: {charactersCount - consoantesCount - vogaisCount}")
                           
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

ar = Arquivo()
ar.charactersDescribe()