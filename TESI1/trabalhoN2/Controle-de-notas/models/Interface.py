import sqlite3
import tkinter as tk
from tkinter import BOTH, EW, LEFT, RIGHT, TOP, ttk, messagebox as msg
from turtle import width


from Notas import Notas

from Configurations import Configurations
from Login import Login
from Aluno import Aluno
from Connection import Connection
from Professor import Professor
from Disciplinas import Disciplinas
from Usuario import Usuario
from Treeview import Treeview
from Functions import Functions

from datetime import date


class Display:

    def __init__(self, master):
        self.display = master
        self.larguraTotal = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()
        self.display.minsize(100,100)
        self.display.title("Controle de Notas Acadêmico")
        self.userSession = Login()
        self.bd = Connection()
        self.createtvw = Treeview()
        self.function = Functions()
        self.currentTime = date.today()
        self.currentTime = self.currentTime.year
        

        # if not self.userSession.isLogged:
        self.display.withdraw()

        def tvw_disciplinas(master):
            self.colunasDisciplinas = self.createtvw.columnsgenerator('id','nome','semestre','professor','codigo')
            self.tvwDisciplinas = self.createtvw.instancetvw(master, self.colunasDisciplinas)
            self.tvwDisciplinas.pack(side=tk.TOP,fill=BOTH,expand=True)
            self.createtvw.heading(self.tvwDisciplinas, self.colunasDisciplinas)
            self.createtvw.column(self.tvwDisciplinas, self.colunasDisciplinas)

        def atualizar_alunos():...
                
        def configurations(key: str = ...):
            self.isConfiguration = self.bd.getConfigurationsByUser(self.userSession.getUserId)
            # Tela para fazer a configuração inicial
            self.toplevelConfigurations = tk.Toplevel(self.display)
            self.toplevelConfigurations.title("Configurações iniciais")
            self.toplevelConfigurations.geometry("500x100")

            self.labelConfigurations1 = tk.Label(self.toplevelConfigurations,
            text="Bem vindo!", font=10)
            self.labelConfigurations1.pack(side=tk.TOP)

            self.labelConfigurations2 = tk.Label(self.toplevelConfigurations,
            text="Indique a quantidade de atividades que fará para N1 e para N2", font=10)
            self.labelConfigurations2.pack(side=tk.TOP)

            self.frameConfigurations = tk.Frame(self.toplevelConfigurations)
            self.frameConfigurations.pack(side=tk.LEFT)

            self.labelN1 = tk.Label(self.frameConfigurations, text="Quantidade de atividades para N1:",font="arial 10 bold")
            self.labelN1.grid(row=0,column=0)

            self.EntryN1 = tk.Entry(self.frameConfigurations, width=20)
            self.EntryN1.grid(row=0,column=1)
            self.EntryN1.insert(0, '0')

            self.labelN2 = tk.Label(self.frameConfigurations, text="Quantidade de atividades para N2:",font="arial 10 bold")
            self.labelN2.grid(row=1,column=0)

            self.EntryN2 = tk.Entry(self.frameConfigurations, width=20)
            self.EntryN2.grid(row=1,column=1)
            self.EntryN2.insert(0, '0')

            def saveConfiguration():
                self.N1amount = self.EntryN1.get()
                self.N2amount = self.EntryN2.get()
                
                if msg.askyesno('Confirme os dados',
                f'Quantidade de atividades para N1: {self.N1amount} \nQuantidade de atividades para N2: {self.N2amount}'):
                    
                    self.configs = Configurations(str(self.N1amount), str(self.N2amount), str(self.userSession.getUserId))
                    self.bd.inserir(self.configs)

                    self.toplevelConfigurations.destroy()
                    tela_principal()

            def alterConfiguration():
                self.N1amount = self.EntryN1.get()
                self.N2amount = self.EntryN2.get()
                
                if msg.askyesno('Confirme os dados',
                    f'Quantidade de atividades para N1: {self.N1amount} \nQuantidade de atividades para N2: {self.N2amount}'):

                    self.bd.alterConfigurationsByUser(self.userSession.getUserId,self.N1amount,self.N2amount)
                    self.toplevelConfigurations.destroy()
                    msg.showinfo('Aviso!','Reinicie a aplicação para aplicar as mudanças!',parent=self.display)

            if key == 'alter':
                self.buttonSaveConfiguration = tk.Button(self.frameConfigurations, text="Salvar!",command=alterConfiguration,bg='#B6C4A2',font="arial 10 bold")
            else:
                self.buttonSaveConfiguration = tk.Button(self.frameConfigurations, text="Salvar!",command=saveConfiguration,bg='#B6C4A2',font="arial 10 bold")
            self.buttonSaveConfiguration.grid(row=0,column=2,rowspan=2)  
        
        def setProfessor():
            self.toplevelWhoP = tk.Toplevel()
            self.toplevelWhoP.minsize(200,200)

            self.labelWhoP = tk.Label(self.toplevelWhoP,text="Qual professor é você?",font="arial 8 bold")
            self.labelWhoP.pack(side=tk.TOP,expand=True)

            self.colunaWhoP = self.createtvw.columnsgenerator('id','nome')
            self.tvwProfessores = self.createtvw.instancetvw(self.toplevelWhoP,self.colunaWhoP)
            self.tvwProfessores.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
            self.createtvw.heading(self.tvwProfessores,self.colunaWhoP)
            self.createtvw.column(self.tvwProfessores,self.colunaWhoP)

            self.createtvw.atualizar(self.tvwProfessores,self.bd.getAllProfessores())

            def selecionar():
                self.valor = self.createtvw.selecionar(self.toplevelWhoP,self.tvwProfessores)
                self.bd.alterProfessorInUsuariobyId(self.userSession.getUserId,self.valor[0])
                self.userSession.user.professor = self.valor[0]
                msg.showinfo('Sucesso!',f'Usuário associado ao professor {self.valor[1]} com sucesso',parent=self.toplevelWhoP)
                self.toplevelWhoP.destroy()
                tela_principal()

            self.framebottom = tk.Frame(self.toplevelWhoP)
            self.framebottom.pack(side=tk.BOTTOM)

            self.buttonSelec = tk.Button(self.framebottom,text="Selecionar",bg='#B6C4A2',font="arial 10 bold",width=15,command=selecionar)
            self.buttonSelec.grid(row=0,column=0)

            def confirmar():
                if not self.entryNomeProfessor.get(): msg.showerror('Não permitido','Digite seu nome completo!',parent=self.toplevelWhoP)
                else: 
                    self.newProfessor = Professor(self.entryNomeProfessor.get())
                    self.bd.inserir(self.newProfessor)
                    self.entryNomeProfessor.delete(0,"end")
                    self.createtvw.atualizar(self.tvwProfessores,self.bd.getAllProfessores())

            def cadastro():
                self.framecadastro = tk.Frame(self.toplevelWhoP)
                self.framecadastro.pack(side=tk.BOTTOM)

                self.labelNomeProfessor = tk.Label(self.framecadastro,text="Nome Completo:",font="arial 9 italic")
                self.labelNomeProfessor.grid(row=0,column=0)

                self.entryNomeProfessor = tk.Entry(self.framecadastro,width=50)
                self.entryNomeProfessor.grid(row=0,column=1)

                self.buttonSalvar = tk.Button(self.framecadastro,text="Salvar!",font="arial 10 bold",bg='#B6C4A2',command=confirmar)
                self.buttonSalvar.grid(row=0,column=2)

            

            self.buttonCadastrarse = tk.Button(self.framebottom,text="Cadastrar-se",bg='#B6C4A2',font="arial 10 bold",width=15,command=cadastro)
            self.buttonCadastrarse.grid(row=0,column=1)

        def cadastrarDisciplina(master):
                    # self.toplevelDisciplinas.iconify()
                    self.toplevelCadastroDisciplina = tk.Toplevel(master)
                    self.toplevelCadastroDisciplina.title("Cadastro de disciplinas")
                    self.toplevelCadastroDisciplina.minsize(200,100)

                    self.labelNomeDisciplina = tk.Label(self.toplevelCadastroDisciplina, text="Nome da Disciplina:",font="arial 9 bold")
                    self.labelSemetreDisciplinas = tk.Label(self.toplevelCadastroDisciplina, text="Semestre da Disciplina:",font="arial 9 bold")
                    self.labelAnoDisciplinas = tk.Label(self.toplevelCadastroDisciplina, text="Ano da Disciplina:",font="arial 9 bold")
                    self.labelCodigoDisciplinas = tk.Label(self.toplevelCadastroDisciplina, text="Codigo da Disciplina:",font="arial 9 bold")
                    self.labelamountN1 = tk.Label(self.toplevelCadastroDisciplina, text="Quantidade de Parciais para N1:",font="arial 9 bold")
                    self.labelamountN2 = tk.Label(self.toplevelCadastroDisciplina, text="Quantidade de Parciais para N2:",font="arial 9 bold")

                    self.labelNomeDisciplina.grid(row=0,column=0)
                    self.labelSemetreDisciplinas.grid(row=1,column=0)
                    self.labelAnoDisciplinas.grid(row=2,column=0)
                    self.labelCodigoDisciplinas.grid(row=3,column=0)
                    self.labelamountN1.grid(row=4,column=0)
                    self.labelamountN2.grid(row=5,column=0)

                    self.entryNomeDisciplina = tk.Entry(self.toplevelCadastroDisciplina,width=100)
                    self.entrySemetreDisciplinas = tk.Entry(self.toplevelCadastroDisciplina,width=100)

                    self.entryAnoDisciplinas = tk.Entry(self.toplevelCadastroDisciplina,width=100)
                    self.entryAnoDisciplinas.insert(0, self.currentTime)

                    self.entryCodigoDisciplinas = tk.Entry(self.toplevelCadastroDisciplina,width=100)
                    self.entryamountN1 = tk.Entry(self.toplevelCadastroDisciplina,width=100)
                    self.entryamountN1.insert(0, '1')

                    self.entryamountN2 = tk.Entry(self.toplevelCadastroDisciplina,width=100)
                    self.entryamountN2.insert(0, '1')

                    self.entryNomeDisciplina.grid(row=0,column=1)
                    self.entrySemetreDisciplinas.grid(row=1,column=1)
                    self.entryAnoDisciplinas.grid(row=2,column=1)
                    self.entryCodigoDisciplinas.grid(row=3,column=1)
                    self.entryamountN1.grid(row=4,column=1)
                    self.entryamountN2.grid(row=5,column=1)

                    def confirmar():
                    
                        self.isEmpty = self.function.isFieldsEmpty(
                            self.entryNomeDisciplina,
                            self.entrySemetreDisciplinas,
                            self.entryAnoDisciplinas,
                            self.entryCodigoDisciplinas,
                            self.entryamountN2,
                            self.entryamountN1)

                        if self.isEmpty: msg.showerror('Operação não permitida',
                            'Preencha todos os campos para continuar', parent=self.toplevelCadastroDisciplina)
                        else:
                            self.Vnomedisciplina = self.entryNomeDisciplina.get()
                            self.Vsemestredisciplina = self.entrySemetreDisciplinas.get()
                            self.Vanodisciplina = self.entryAnoDisciplinas.get()
                            self.Vcodigodisciplina = self.entryCodigoDisciplinas.get()
                            self.Vprofessordisciplina = self.userSession.getProfessorID
                            
                            self.newDisciplina = Disciplinas(self.Vnomedisciplina,
                                self.Vanodisciplina,
                                self.Vsemestredisciplina,
                                self.Vprofessordisciplina,
                                self.Vcodigodisciplina)
                            self.bd.inserir(self.newDisciplina)
                            msg.showinfo('Sucesso','Disciplina cadastrada!',parent=self.toplevelCadastroDisciplina)
                            self.lastdisciplina = self.bd.getIdOfLastTable('disciplinas')
                            self.configs = Configurations(self.entryamountN1.get(),self.entryamountN2.get(),self.lastdisciplina[0][0])
                            self.bd.inserir(self.configs)
                            self.toplevelCadastroDisciplina.destroy()


                    self.buttonConfirmar = tk.Button(self.toplevelCadastroDisciplina,text='confirmar',command=confirmar,bg='#B6C4A2',font="arial 10 bold")
                    self.buttonConfirmar.grid(row=0,column=2)

        def display_principal(disciplinaID):
            self.display.withdraw()
            self.topleveldisplay = tk.Toplevel()
            self.topleveldisplay.geometry("{0}x{1}+0+0".format(self.larguraTotal, self.alturaTotal))

            # self.frameAlunos = tk.Frame(self.topleveldisplay)
            # self.frameAlunos.pack(side=tk.TOP,expand=True)

            self.userConfigurations = self.bd.getConfigurationsByDisciplina(disciplinaID)
            self.configs = self.bd.getConfigurationsByDisciplina(disciplinaID)
            self.configs = self.configs[0]

            # self.labelNome = tk.Label(self.frameAlunos,text="Nome:",font="arial 10 italic")
            # self.labelNome.grid(row=0,column=0)

            # self.entryNome = tk.Entry(self.frameAlunos,width=60,font='arial 9 bold')
            # self.entryNome.grid(row=0,column=1)

            # self.entrys = []
            # self.var = 0
            # self.yar =1

            # for i in range(1,self.configs[1]+1):
            #     self.labelatv = tk.Label(self.frameAlunos,text=f"atvN1.{i}:",font="arial 10 italic")
            #     self.labelatv.grid(row=1,column=self.var)
            #     self.var += 2
            #     self.entryatv = tk.Entry(self.frameAlunos,width=10,font='arial 9 bold')
            #     self.entryatv.grid(row=1,column=self.yar)
            #     self.entrys.append(self.entryatv)
            #     self.yar += 2

            # for i in range(1,self.configs[2]+1):
            #     self.labelatv = tk.Label(self.frameAlunos,text=f"atvN1.{i}:",font="arial 10 italic")
            #     self.labelatv.grid(row=2,column=self.var)
            #     self.var += 2
            #     self.entryatv = tk.Entry(self.frameAlunos,width=10,font='arial 9 bold')
            #     self.entryatv.grid(row=2,column=self.yar)
            #     self.entrys.append(self.entryatv)
            #     self.yar += 2
                
            # self.labelProvaFinal = tk.Label(self.frameAlunos,text="Proval Final:",font="arial 8 italic")

            def voltar():
                self.topleveldisplay.destroy()
                self.toplevelPreNotas.destroy()
                self.display.deiconify()

            self.voltar = tk.Button(self.topleveldisplay,text='voltar',bg='#B6C4A2',font="arial 10 bold",width=20,command=voltar)
            self.voltar.pack(side=tk.TOP)

            #Contruindo Treeview para exibição dos alunos
            self.alunosByDisciplina = self.bd.getAlunosForTvw(disciplinaID)


            self.colunasTvwAlunos = self.createtvw.columnsgenerator(
                'id',
                'nome',
                f'N1={self.userConfigurations[0][1]}',
                'N1',f'N2={self.userConfigurations[0][2]}',
                'N2',
                'Media Final',
                'Prova Final',
                'Situação Final')
            self.tvwAlunos = self.createtvw.instancetvw(self.topleveldisplay,self.colunasTvwAlunos)
            self.tvwAlunos.pack(side=tk.TOP,fill=BOTH,expand=True)
            self.createtvw.heading(self.tvwAlunos,self.colunasTvwAlunos)
            self.createtvw.column(self.tvwAlunos,self.colunasTvwAlunos)


            self.alunos = self.bd.getAlunosForTvw(disciplinaID)
            self.alunosinsercao = []

            for aluno in self.alunos:
                print(aluno)
                self.listaAluno = []
                self.listaAluno.append(aluno[0])
                self.listaAluno.append(aluno[1])
                self.valorN1 = 0
                self.valorN2 = 0
                self.mediaFinal = 0
                self.situacaoFinal = ''
                for notaN1 in range(1,int(self.configs[1]+1)):

                    self.nota = self.bd.getNotaByAlunoAndIdentificadorAndDisciplina(
                        disciplinaID,aluno[0],f'atvN1.{notaN1}'
                    )
                    try:
                        self.listaAluno.append(self.nota[0][0])
                        self.valorN1 += float(self.nota[0][0])
                    except: ...
                try:
                    self.valorN1 = self.valorN1 / int(self.configs[1])
                    self.mediaFinal += self.valorN1
                    self.listaAluno.append(f'{self.valorN1:.2f}')
                except: ...

                for notaN2 in range(1,int(self.configs[2]+1)):

                    self.nota = self.bd.getNotaByAlunoAndIdentificadorAndDisciplina(
                        disciplinaID,aluno[0],f'atvN2.{notaN2}'
                    )
                    try:
                        self.listaAluno.append(self.nota[0][0])
                        self.valorN2 += float(self.nota[0][0])
                    except: ...
                try:
                    self.valorN2 = self.valorN2 / int(self.configs[2])
                    self.listaAluno.append(f'{self.valorN2:.2f}')
                    self.mediaFinal += self.valorN2
                except: ...

                self.mediaFinal = self.mediaFinal/2
                self.listaAluno.append(self.mediaFinal)

                if self.mediaFinal < 8:
                    self.listaAluno.append('final')
                else:
                    self.listaAluno.append('')
                    
                if self.mediaFinal >= 8:
                    self.listaAluno.append('Aprovado')
                else:
                    self.listaAluno.append('Fzr calculo ainda')
                    
                self.alunosinsercao.append(self.listaAluno)

            self.createtvw.atualizar(self.tvwAlunos,self.alunosinsercao)


        def cadastrar_aluno():
                self.isEmpty = self.function.isFieldsEmpty(
                    self.entryNomeAluno,
                    self.entryMatriculaAluno,
                )
                if self.isEmpty: msg.showerror("Operação cancelada!","Nome e Matrícula são obrigatórios!",parent=self.display)
                else:
                    self.aluno = Aluno(self.entryNomeAluno.get(),self.entryMatriculaAluno.get(),self.entryTelefoneAluno.get(),self.entryEmailAluno.get())
                    self.entryNomeAluno.delete(0,"end")
                    self.entryMatriculaAluno.delete(0,"end")
                    self.entryTelefoneAluno.delete(0,"end")
                    self.entryEmailAluno.delete(0,"end")
                    self.bd.inserir(self.aluno)
                    if self.idDisciplina:
                        self.valor = self.bd.getIdOfLastTable('aluno')
                        self.bd.operation(f"INSERT INTO alunodisciplinas(aluno,disciplina) VALUES('{self.valor[0][0]}','{self.idDisciplina}')")
                        self.configs = self.bd.getConfigurationsByDisciplina(self.idDisciplina)
                        self.configs = self.configs[0]
                        
                        for parcialN1 in range(0,int(self.configs[1])):
                            self.bd.operation(
                                f"INSERT INTO notas(disciplina,aluno,nota,identificador) VALUES('{self.idDisciplina}','{self.valor[0][0]}','0.00','atvN1.{parcialN1+1}')"
                            )

                        for parcialN2 in range(0,int(self.configs[2])):
                            self.bd.operation(
                                f"INSERT INTO notas(disciplina,aluno,nota,identificador) VALUES('{self.idDisciplina}','{self.valor[0][0]}','0.00','atvN2.{parcialN2+1}')"
                            )
                        


                    msg.showinfo("Sucesso","Aluno cadastrado com sucesso!",parent=self.display)

        def associar():
                self.toplevelDisciplinas = tk.Toplevel(self.display)
                self.toplevelDisciplinas.title("associação de alunos")
                self.toplevelDisciplinas.minsize(400,300)

                self.frameAssociar = tk.Frame(self.toplevelDisciplinas)
                self.frameAssociar.pack(side=tk.TOP)

                self.labelNomeD = tk.Label(self.frameAssociar,text="Nome:")
                self.labelAnoD = tk.Label(self.frameAssociar,text="Ano:")
                self.labelSemestreD = tk.Label(self.frameAssociar,text="Semestre:")

                self.entryNomeD = tk.Entry(self.frameAssociar,width=50)
                self.entryAnoD = tk.Entry(self.frameAssociar,width=10)
                self.entrySemestreD = tk.Entry(self.frameAssociar,width=10)

                self.labelNomeD.grid(row=0,column=0)          
                self.entryNomeD.grid(row=0,column=1)

                self.labelAnoD.grid(row=0,column=2)               
                self.entryAnoD.grid(row=0,column=3)                

                self.labelSemestreD.grid(row=0,column=4)          
                self.entrySemestreD.grid(row=0,column=5)

                def filtrar():
                    self.disciplinasFiltradas = self.bd.getDisciplinasForTvwByProfessor(
                        self.userSession.getProfessorID,
                        semestre=self.entrySemestreD.get(),
                        ano=self.entryAnoD.get(),
                        nome=self.entryNomeD.get()
                    )
                    self.createtvw.atualizar(self.tvwassociar,self.disciplinasFiltradas)

                self.buttonFiltrar = tk.Button(self.frameAssociar, text="filtrar",command=filtrar,bg='#FFD3BA',font="arial 9 bold")
                self.buttonFiltrar.grid(row=0,column=6)

                self.colunastvwassociar = self.createtvw.columnsgenerator('id','nome','ano','semestre')
                self.tvwassociar = self.createtvw.instancetvw(self.toplevelDisciplinas,self.colunastvwassociar)
                self.tvwassociar.pack(fill=tk.BOTH)
                self.createtvw.heading(self.tvwassociar,self.colunastvwassociar)
                self.createtvw.column(self.tvwassociar,self.colunastvwassociar)

                def completar():
                    self.valor = self.createtvw.selecionar(self.toplevelDisciplinas,self.tvwassociar)
                    print(self.valor)
                    if self.valor:
                        self.idDisciplina = self.valor[0]
                        self.entryDisciplina['state'] = 'normal'
                        self.entryDisciplina.delete(0,"end")
                        self.entryDisciplina.insert(0,self.valor[1])
                        self.entryDisciplina['state'] = 'disabled'
                    

                self.buttonAssociar = tk.Button(self.frameAssociar,text="Associar",font="arial 9 bold",width=12,command=completar,bg='#B6C4A2')
                self.buttonAssociar.grid(row=0,column=7)

                self.disciplinasByprofessor = self.bd.getDisciplinasbyProfessor(self.userSession.getProfessorID,ano=self.currentTime)
                self.createtvw.atualizar(self.tvwassociar,self.disciplinasByprofessor)

        def associacoes():
            self.toplevelassociacoes = tk.Toplevel(self.display)
            self.toplevelassociacoes.minsize(1200,500)
            self.toplevelassociacoes.title("Painel de Controle de Associações")

            self.labelass = tk.Label(self.toplevelassociacoes,text="Selecione o aluno e a disciplina e clique em associar",font="arial 11 italic bold")
            self.labelass.pack(side=tk.TOP)

            self.tvwalunos = self.createtvw.instancetvw(self.toplevelassociacoes,['id','nome','matricula','telefone','email','responsavel'])
            self.tvwalunos.pack(side=tk.LEFT,fill=tk.BOTH)
            self.createtvw.heading(self.tvwalunos,['id','nome','matricula','telefone','email','responsavel'])
            self.createtvw.column(self.tvwalunos,['id','nome','matricula','telefone','email','responsavel'])

            self.createtvw.atualizar(self.tvwalunos,self.bd.getAllAlunos())

            def ass():
                self.disciplina = self.createtvw.selecionar(self.toplevelassociacoes,self.tvwassociar)
                if self.disciplina and self.tvwalunos.selection():
                    for dados in self.createtvw.selecionarVarios(self.tvwalunos):
                        if self.bd.getAlunoDisciplinas(dados[0],self.disciplina[0]):
                            pass
                        else:
                            self.bd.operation(f"INSERT INTO alunodisciplinas(aluno,disciplina) VALUES('{dados[0]}','{self.disciplina[0]}')")
                    msg.showinfo("Sucesso!","Alunos associados com sucesso!",parent=self.toplevelassociacoes)

            self.buttonasss = tk.Button(self.toplevelassociacoes,text='Associar',command=ass,bg='#B6C4A2',font="arial 10 bold")
            self.buttonasss.pack(side=tk.LEFT)

            self.colunastvwassociar = self.createtvw.columnsgenerator('id','nome','ano','semestre')
            self.tvwassociar = self.createtvw.instancetvw(self.toplevelassociacoes,self.colunastvwassociar)
            self.tvwassociar.pack(side=tk.LEFT,fill=tk.BOTH)
            self.createtvw.heading(self.tvwassociar,self.colunastvwassociar)
            self.createtvw.column(self.tvwassociar,self.colunastvwassociar)

            self.createtvw.atualizar(self.tvwassociar,self.bd.getDisciplinasForTvwByProfessor(self.userSession.getProfessorID))


        def notas():
            self.display.withdraw()
            self.toplevelPreNotas = tk.Toplevel(self.display)

            self.colunastvwassociar = self.createtvw.columnsgenerator('id','nome','ano','semestre')
            self.tvwassociar = self.createtvw.instancetvw(self.toplevelPreNotas,self.colunastvwassociar)
            self.tvwassociar.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
            self.createtvw.heading(self.tvwassociar,self.colunastvwassociar)
            self.createtvw.column(self.tvwassociar,self.colunastvwassociar)

            self.createtvw.atualizar(self.tvwassociar,self.bd.getDisciplinasForTvwByProfessor(self.userSession.getProfessorID))

            def selecionarD():
                self.valor = self.createtvw.selecionar(self.toplevelPreNotas,self.tvwassociar)
                display_principal(self.valor[0][0])
                

            self.btnSelect = tk.Button(self.toplevelPreNotas,text="SELECIONAR",command=selecionarD,bg='#B6C4A2',font="arial 10 bold")
            self.btnSelect.pack(side=tk.RIGHT)


        def tela_principal():
            self.display.deiconify()
            self.frameprincipal = tk.Frame(self.display)
            self.frameprincipal.pack(side=tk.LEFT)

            self.labelinformacao = tk.Label(self.frameprincipal,text="Cadastre novos alunos aqui:",font=10)
            self.labelinformacao.grid(row=0,column=0,columnspan=3)

            self.labelNomeAluno = tk.Label(self.frameprincipal, text="Nome completo:")
            self.labelMatriculaAluno = tk.Label(self.frameprincipal, text="Nº de Matrícula:")
            self.labelTelefoneAluno = tk.Label(self.frameprincipal, text="Nº de telefone (OPICIONAL):")
            self.labelEmailAluno = tk.Label(self.frameprincipal, text="Email (OPICIONAL):")
            self.labelDisciplina = tk.Label(self.frameprincipal, text="Disciplina:")

            self.labelNomeAluno.grid(row=1,column=0)
            self.labelMatriculaAluno.grid(row=2,column=0)
            self.labelTelefoneAluno.grid(row=3,column=0)
            self.labelEmailAluno.grid(row=4,column=0)
            self.labelDisciplina.grid(row=5,column=0)

            self.entryNomeAluno = tk.Entry(self.frameprincipal,width=60,font="arial 8 bold")
            self.entryMatriculaAluno = tk.Entry(self.frameprincipal,width=60,font="arial 8 bold")
            self.entryTelefoneAluno = tk.Entry(self.frameprincipal,width=60,font="arial 8 bold")
            self.entryEmailAluno = tk.Entry(self.frameprincipal,width=60,font="arial 8 bold")
            self.entryDisciplina = tk.Entry(self.frameprincipal,width=60,font="arial 8 bold",state="disabled")

            self.entryNomeAluno.grid(row=1,column=1)
            self.entryMatriculaAluno.grid(row=2,column=1)
            self.entryTelefoneAluno.grid(row=3,column=1)
            self.entryEmailAluno.grid(row=4,column=1)
            self.entryDisciplina.grid(row=5,column=1)

            self.idDisciplina = None
                  
            self.buttonCadastrarAluno = tk.Button(self.frameprincipal,text="Salvar!",command=cadastrar_aluno,bg='#B6C4A2',font="arial 10 bold")
            self.buttonCadastrarAluno.grid(row=1,column=2)

            self.buttonAssociar = tk.Button(self.frameprincipal,text="Associar aluno à disciplina!",command=associar,bg='#B6C4A2',font="arial 10 bold")
            self.buttonAssociar.grid(row=5,column=2)

            self.frameBotoes = tk.Frame(self.display)
            self.frameBotoes.pack(side=tk.TOP)

            self.cadastrarDisciplina = tk.Button(self.frameBotoes,text="Cadastrar Disciplinas",command=lambda:cadastrarDisciplina(self.display),bg='#B6C4A2',font="arial 10 bold")
            self.cadastrarDisciplina.grid(row=0,column=0)

            self.assdeAl = tk.Button(self.frameBotoes,text="Associação de Alunos",command=associacoes,bg='#B6C4A2',font="arial 10 bold")
            self.assdeAl.grid(row=1,column=0)

            self.buttonNotas = tk.Button(self.frameBotoes,text="Acessar notas",command=notas,bg='#B6C4A2',font="arial 10 bold")
            self.buttonNotas.grid(row=2,column=0)

        def logar():
            if self.function.isFieldsEmpty(
                    self.userEntryLogin,
                    self.passwordEntryLogin):
                msg.showerror("Operação não permitida","Informe um usuario e senha",parent=self.passwordEntryLogin)
            else:
                self.usernameLogin = self.userEntryLogin.get()
                self.passwordLogin = self.passwordEntryLogin.get()
                self.isUser = self.bd.getUserByUserName(self.usernameLogin)
                if not self.isUser:
                    msg.showerror("","Usuário não encontrado!", parent=self.toplevelLogin)
                else:
                    self.hash = self.isUser[0][1]
                    self.isTrue = self.userSession.isKeyTrue(self.passwordLogin,self.hash[2:len(self.hash)-1:])                    
                    if self.isTrue:
                        self.userSession.login()

                        # Construção de um objeto usuário para ser inserido no cache de sessão do usuário
                        self.userLogin = Usuario(self.isUser[0][1],self.isUser[0][2],self.isUser[0][3])
                        self.userLogin.id = self.isUser[0][0]
                        self.userSession.set_user(self.userLogin)

                        # Assim que fizer login, será instânciado algumas variável globais
                        self.disciplinaAtual = self.bd.getDisciplinasbyProfessor(self.userSession.getProfessorID,ano=self.currentTime) #Primeira disciplina que o banco devolver, no ano atual

                        self.toplevelLogin.destroy()

                        # Verificando se é o primeiro login do usuario
                        if self.isUser[0][3] == 'None':
                            setProfessor()
                            
                        else:
                            tela_principal()
                    else:
                        msg.showerror("","Usuário ou senha incorretas!", parent=self.toplevelLogin)

        def cadastro():
            self.toplevelLogin.withdraw()
            self.toplevelCadastro = tk.Toplevel(self.toplevelLogin)
            self.toplevelCadastro.title("Cadastro de novo usuário")
            self.toplevelCadastro.minsize(100,100)

            self.frametoplevelCadastro = tk.Frame()
            self.frametoplevelCadastro.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.usernameLabel = tk.Label(self.toplevelCadastro, text="username:")
            self.usernameEntry = tk.Entry(self.toplevelCadastro, width=60)
            self.usernameLabel.grid(row=0,column=0)
            self.usernameEntry.grid(row=0,column=1, sticky=EW)

            self.passwordLabel = tk.Label(self.toplevelCadastro, text="password:")
            self.passwordEntry = tk.Entry(self.toplevelCadastro, width=60)
            self.passwordLabel.grid(row=1,column=0)
            self.passwordEntry.grid(row=1,column=1)

            def confirmarCadastro():
                username = self.usernameEntry.get()
                password = self.passwordEntry.get()

                self.isEmpty = self.function.isFieldsEmpty(
                    self.usernameEntry,
                    self.passwordEntry)
                    
                if self.isEmpty:
                    msg.showerror('Operação não permitida','Preencha todos os campos para continuar!',parent=self.toplevelCadastro)
                else:
                    try:
                        self.encriptedPassword = self.userSession.encript(password)
                        self.newUser = Usuario(self.encriptedPassword,username,'None')
                        self.bd.inserir(self.newUser)
                        msg.showinfo("Sucesso!","Usuário cadastrado com sucesso!",parent=self.toplevelCadastro)
                        self.toplevelCadastro.destroy()
                        self.toplevelLogin.deiconify()
                    except sqlite3.IntegrityError:
                        msg.showerror('Operação não permitida','Já existe um usuário com esse username!',parent=self.toplevelCadastro)
                
            self.buttonCadastrar = tk.Button(self.toplevelCadastro, text="Cadastrar!", command=confirmarCadastro)
            self.buttonCadastrar.grid(row=0,column=2)

            def cancel():
                self.toplevelCadastro.destroy()
                self.toplevelLogin.deiconify()

            self.buttonCancelCadastro = tk.Button(self.toplevelCadastro, text="Cancelar!", command=cancel)
            self.buttonCancelCadastro.grid(row=1,column=2)
        
        self.toplevelLogin = tk.Toplevel()
        self.toplevelLogin.title("Login")
        self.toplevelLogin.minsize(1,1)

        self.frametoplevelLogin = tk.Frame(self.toplevelLogin)
        self.frametoplevelLogin.pack(side=tk.LEFT,fill=BOTH, expand=True)

        self.userLabelLogin = tk.Label(self.frametoplevelLogin, text="username:",font="Arial 10 bold")
        self.userEntryLogin = tk.Entry(self.frametoplevelLogin,font="arial 10 italic")
        self.userLabelLogin.grid(row = 0, column = 0)
        self.userEntryLogin.grid(row = 0, column = 1, ipadx=30)

        self.passwordLabelLogin = tk.Label(self.frametoplevelLogin, text="password:",font="Arial 9 bold")
        self.passwordEntryLogin = tk.Entry(self.frametoplevelLogin,show="*")
        self.passwordLabelLogin.grid(row = 1, column = 0)
        self.passwordEntryLogin.grid(row = 1, column = 1, ipadx=30)

        self.buttonLogin = tk.Button(self.frametoplevelLogin, text="Login", command=logar,bg='#B6C4A2',font="arial 10 bold")
        self.buttonLogin.grid(row = 2, column = 0, sticky=EW)

        self.buttonCadastro = tk.Button(self.frametoplevelLogin, text="Criar cadastro", command=cadastro,bg='#B6C4A2',font="arial 10 bold")
        self.buttonCadastro.grid(row = 2, column = 1, sticky=EW)

app = tk.Tk()
Display(app)
app.mainloop()