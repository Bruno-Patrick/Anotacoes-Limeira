class Medias:
    def __init__(self):
        pass

    def medias(self):
        arquivo1 = str(input("\nDIGITE O NOME DO ARQUIVO DOS ALUNOS\n"+
                f"(não é necessário informar extensão '.txt')\nNome do Arquivo: \n"))
        A1 = arquivo1
        arquivo2 = str(input("\nDIGITE O NOME DO ARQUIVO DAS NOTAS\n"+
                f"(não é necessário informar extensão '.txt')\nNome do Arquivo: \n"))
        A2 = arquivo2
            
        with open(f'Atividade sobre manipulação de arquivos\{arquivo2}.txt', 'r') as arquivo2:
            notas = []
            leitura = arquivo2.readlines()
            for i in leitura:
                linha = i.split()
                media = 0
                for j in linha:
                    j = float(j)
                    media += j
                media = media/len(linha)
                notas.append(media)

        with open(f'Atividade sobre manipulação de arquivos\{arquivo1}.txt', 'r') as arquivo1:
            alunos = []
            leituraAluno = arquivo1.readlines()
            for i in leituraAluno:
                alunos.append(i)
        with open(f'Atividade sobre manipulação de arquivos\medias_alunos.txt', 'w') as medias:
            for i in range(0,len(alunos)):
                medias.write(f"{alunos[i]}  MEDIA: {notas[i]:.2f}\n")

    def ler_media(self):
        notas = []
        with open(f'Atividade sobre manipulação de arquivos\medias_alunos.txt', 'r') as medias:
            leitura = medias.readlines()
            for i in leitura:
                linha = i.split()
                for j in range(0, len(linha)):
                    try:
                        nota = float(linha[j])
                        notas.append(nota)
                    except:
                        pass
        notas.sort(reverse=True)
        print(notas)