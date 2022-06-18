class Arquivo:
    def __init__(self):
        pass

    def escrever(self, arquivo='', content=''):
        if (arquivo) or (content):
            nome = arquivo
            texto = content
        else:
            nome = str(input("DIGITE O NOME DO ARQUIVO\n"+
                f"(não é necessário informar extensão '.txt')\nNome do Arquivo: \n"))
            texto = str(input("Digite o texto: "))

        with open(f'Atividade sobre manipulação de arquivos\{nome}.txt', 'a') as nome:
            nome.write(f'{texto}\n')

    def vogais(self, palavra):
        vogais = 0
        lista_vogais = ['a','e','i','o','u']
        for char in palavra:
            for voga in lista_vogais:
                if char == voga:
                    vogais += 1
                else:
                    pass
        return vogais
    
    def consoantes(self, palavra):
        consoante = 0
        consoante_vogais = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
        'l', 'm', 'n', 'p', 'q', 'r', 's',
        't', 'v', 'w', 'x', 'y', 'z']
        for char in palavra:
            for conso in consoante_vogais:
                if char == conso:
                    consoante += 1
                else:
                    pass
        return consoante

    def ler(self):
        qnt = int(input("Quantos arquivos você irá passar?\nQuantidade:"))
        for i in range(0,qnt):
            nome = str(input("\nDIGITE O NOME DO ARQUIVO\n"+
                    f"(não é necessário informar extensão '.txt')\nNome do Arquivo: "))
            try:
                with open(f'Atividade sobre manipulação de arquivos\{nome}.txt', 'r') as nome:
                    linhas = nome.readlines()
                    linhasQNT = len(linhas)
                    palavrasQNT = 0
                    caracteresQNT = 0
                    vogais = 0
                    consoantes = 0
                    for i in linhas:
                        linha = i.split()
                        for j in linha:
                            palavras = j.split()
                            palavrasQNT += len(palavras)
                            for k in palavras:
                                char = list(k)
                                vogais += self.vogais(char)
                                consoantes += self.consoantes(char)
                                caracteresQNT += len(char)
                with open(f'Atividade sobre manipulação de arquivos\SAIDAS.txt', 'a') as saida:
                    saida.write(f'A quantidade de linhas é {linhasQNT}\n')
                    saida.write(f'A quantidade de palavras é {palavrasQNT}\n')
                    saida.write(f'A quantidade de caracteresQNT é {caracteresQNT}\n')
                    saida.write(f'A quantidade de vogais é {vogais}\n')
                    saida.write(f'A quantidade de consoantes é {consoantes}\n')
                    saida.write(f'A quantidade de caracteres especiais é {caracteresQNT-vogais-consoantes}\n')
            except FileNotFoundError:
                print("Arquivo não encontrado! Crie-o primeiro.")

    def compara(self):
        arquivo1 = input("DIGITE O NOME DO ARQUIVO\n"+
                f"(não é necessário informar extensão '.txt')\nNome do Arquivo: ")

        arquivo2 = str(input("DIGITE O NOME DO ARQUIVO\n"+
                f"(não é necessário informar extensão '.txt')\nNome do Arquivo: "))
        try:
            with open(f'Atividade sobre manipulação de arquivos\{arquivo1}.txt', 'r') as arquivo1:
                content = arquivo1.read()

                with open(f'Atividade sobre manipulação de arquivos\{arquivo2}.txt', 'r') as arquivo2:
                    content2 = arquivo2.read()
                    if content == content2:
                        print("Os arquivos possuem conteúdo iguais")
                    else:
                        print("Os conteúdos dos arquivos são diferentes")
        except FileNotFoundError:
            print("Arquivo não encontrado! Caso não exista, crie-o primeiro.")

    def substituir(self):
        padrao = str(input("Digite a palavra padrão: \n"))
        substituicao = str(input("Digite a palavra de substituição: \n"))
        arquivo1 = str(input("DIGITE O NOME DO ARQUIVO 1\n"+
                f"(não é necessário informar extensão '.txt')\nNome do Arquivo: \n"))
        A1 = arquivo1
        arquivo2 = str(input("DIGITE O NOME DO ARQUIVO 2\n"+
                f"(não é necessário informar extensão '.txt')\nNome do Arquivo: \n"))
        A2 = arquivo2
        with open(f'Atividade sobre manipulação de arquivos\{arquivo1}.txt', 'r') as arquivo1:
            leitura = arquivo1.read()
            subs = leitura.replace(padrao, substituicao)
            with open(f'Atividade sobre manipulação de arquivos\{A2}.txt', 'w') as arquivo2:
                arquivo2.write(leitura)
        with open(f'Atividade sobre manipulação de arquivos\{A1}.txt', 'w') as arquivo1:
            arquivo1.write(subs)