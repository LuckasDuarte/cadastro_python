from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

from view import *

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# Criando Janela ###############
janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.resizable(width= False, height= False)
janela.configure(background = co9)

################# Dividindo a Janela ###############
Frame_topo = Frame(janela, width = 310, height=50, bg = co2, relief='flat')
Frame_topo.grid(row= 0, column= 0)

Frame_inferior = Frame(janela, width = 310, height=403, bg = co1, relief='flat')
Frame_inferior.grid(row= 1, column= 0, padx=1, sticky=NSEW )

Frame_Direita = Frame(janela, width = 600, height=50, bg = co1, relief='flat')
Frame_Direita.grid(row= 0, column= 1, rowspan=2, padx=1, sticky=NSEW )

################# Label Superior ###############

titulo = Label( Frame_topo, text='Formulário de Consulta', anchor = NW,  bg=co2, font=('Ivy 13 bold'), fg=co1, relief='flat')
titulo.place(x=10, y=20)

global tabela

#Função Inserir
def Inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    data = e_data.get()
    prioridade = e_prioridade.get()
    especialidade = e_espacialidade.get()

    lista = [nome, email, telefone, data, prioridade ,especialidade]

    if nome == "":
        messagebox.showerror(title='Ops!', message='Preencha Todos os campos Corretamente!')
    else:
        Inserir_Informacoes(lista)
        messagebox.showinfo(title='Informação Inserida', message='Informação Acrescentada com Sucesso!')

    e_nome.delete(0, 'end')
    e_email.delete(0, 'end')
    e_telefone.delete(0, 'end')
    e_data.delete(0, 'end')
    e_prioridade.delete(0, 'end')
    e_espacialidade.delete(0, 'end')

    for widget in Frame_Direita.winfo_children():
        widget.destroy()
    
    Mostrar_Tabela()

#Função Atualizar 
def Atualizar():
    try:
        dados_tabela = tabela.focus()
        dicionario_tabela = tabela.item(dados_tabela)
        lista_tabela = dicionario_tabela['values']

        dados_id = lista_tabela[0]

        #Apagando os dados nas entrys
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_data.delete(0, 'end')
        e_prioridade.delete(0, 'end')
        e_espacialidade.delete(0, 'end')

        #Inserindo os Dados nas entrys
        e_nome.insert(0, lista_tabela[1])
        e_email.insert(0, lista_tabela[2])
        e_telefone.insert(0, lista_tabela[3])
        e_data.insert(0, lista_tabela[4])
        e_prioridade.insert(0, lista_tabela[5])
        e_espacialidade.insert(0, lista_tabela[6])

        #Função Atualizar
        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_telefone.get()
            data = e_data.get()
            prioridade = e_prioridade.get()
            especialidade = e_espacialidade.get()

            lista = [nome, email, telefone, data, prioridade ,especialidade, dados_id]

            if lista == '':
                messagebox.showerror(title='Ops!', message='Preencha Todos os campos Corretamente!')
            else:
                Atualizar_Informacoes(lista)
                messagebox.showinfo(title='Informação Atualizada', message='Informação Atualizada com Sucesso!')

            e_nome.delete(0, 'end')
            e_email.delete(0, 'end')
            e_telefone.delete(0, 'end')
            e_data.delete(0, 'end')
            e_prioridade.delete(0, 'end')
            e_espacialidade.delete(0, 'end')

            for widget in Frame_Direita.winfo_children():
                widget.destroy()

            Mostrar_Tabela()
            b_confirmar.destroy()
            b_atualizar = Button(Frame_inferior, width=10,height=2 ,text='Atualizar', bg=co2, anchor='center', fg=co1, relief='raised', font=('Ivy 8 bold'), overrelief='ridge', command=Atualizar)
            b_atualizar.place(x= 110, y= 310)


        b_atualizar.destroy()
        #Botao Para Confirmar alteração
        b_confirmar = Button(Frame_inferior, width=10,height=2 ,text='Confirmar', bg=co2, anchor='center', fg=co1, relief='raised', font=('Ivy 8 bold'), overrelief='ridge', command= update)
        b_confirmar.place(x= 110, y= 310)

    except IndexError:
        messagebox.showerror(title='Erro', message='Selecione o dado na tabela')

#Função Deletar
def Deletar():
    try:
        dados_tabela = tabela.focus()
        dicionario_tabela = tabela.item(dados_tabela)
        lista_tabela = dicionario_tabela['values']

        dados_id = [lista_tabela[0]]

        resposta = messagebox.askquestion(title='Tem Certeza?',message='Deseja deletar esta informação?')
        if resposta == 'yes':
            Deletar_Informacoes(dados_id)
            for widget in Frame_Direita.winfo_children():
                widget.destroy()
            Mostrar_Tabela()
        else:
            pass
    except IndexError:
        messagebox.showerror(title='Erro', message='Selecione o que deseja apagar')

################ Frame Inferior ################
################# Entrada Nome #################

l_nome = Label(Frame_inferior, text='Nome:', anchor=NW, font=('Ivy 10'), bg=co1,relief='flat')
l_nome.place(x=15, y=10)

e_nome = Entry(Frame_inferior, width=45, relief='solid')
e_nome.place(x=15, y=40)

############### Entrada Email ################

l_email = Label(Frame_inferior, text='Email:', anchor=NW, font=('Ivy 10'), bg=co1,relief='flat')
l_email.place(x=15, y=65)

e_email = Entry(Frame_inferior, width=45, relief='solid')
e_email.place(x=15, y=85)

############### Entrada Telefone ############

l_telefone = Label(Frame_inferior, text='Telefone:', anchor=NW, font=('Ivy 10'), bg=co1,relief='flat')
l_telefone.place(x=15, y=115)

e_telefone = Entry(Frame_inferior, width=45, relief='solid')
e_telefone.place(x=15, y=135)

############### Data Consulta ##############

l_data = Label(Frame_inferior, text='Data da Consulta:', anchor=NW, font=('Ivy 10'), bg=co1,relief='flat')
l_data.place(x=10, y=170)

e_data = DateEntry(Frame_inferior, width= 12, background='darkblue')
e_data.place(x = 15, y = 195)

############## Prioridade #####################

l_prioridade = Label(Frame_inferior, text='Prioridade:', anchor=NW, font=('Ivy 10'), bg=co1,relief='flat')
l_prioridade.place(x=185, y=170)

e_prioridade = Entry(Frame_inferior, width=15, relief='solid')
e_prioridade.place(x=175, y=195)

############## Especialidade ##################

l_espacialidade = Label(Frame_inferior, text='Especialista:', anchor=NW, font=('Ivy 10'), bg=co1,relief='flat')
l_espacialidade.place(x=15, y=230)

e_espacialidade = Entry(Frame_inferior, width=45, relief='solid')
e_espacialidade.place(x=15, y=260)

################## Botões #####################

#Inserir
b_inserir = Button(Frame_inferior, width=10,height=2 ,text='inserir', bg=co6, anchor='center', fg=co1, relief='raised', font=('Ivy 8 bold'), overrelief='ridge', command= Inserir)
b_inserir.place(x= 15, y= 310)

#Atualizar
b_atualizar = Button(Frame_inferior, width=10,height=2 ,text='Atualizar', bg=co2, anchor='center', fg=co1, relief='raised', font=('Ivy 8 bold'), overrelief='ridge', command=Atualizar)
b_atualizar.place(x= 110, y= 310)

#Deletar
b_deletar = Button(Frame_inferior, width=10,height=2 ,text='Deletar', bg=co7, anchor='center', fg=co1, relief='raised', font=('Ivy 8 bold'), overrelief='ridge', command=Deletar)
b_deletar.place(x= 210, y= 310)

############### Tabela #####################

def Mostrar_Tabela():

    global tabela

    #Lista para representação
    lista = Acessar_Informacoes()

    #header tabela
    tabela_head  = [ 'Id','Nome', 'Email', 'Telefone', 'Data', 'Prioridade', 'Especialista']


    #tabela
    tabela = ttk.Treeview(Frame_Direita, selectmode='browse', columns=tabela_head, show='headings')

    #Scrollbar Vertical
    vscb = ttk.Scrollbar(Frame_Direita, orient='vertical', command=tabela.yview)

    #Scrollbar Horizontal
    hscb = ttk.Scrollbar(Frame_Direita, orient='horizontal', command=tabela.xview)

    #Configuração Scrollbar
    tabela.configure(yscrollcommand=vscb.set, xscrollcommand=hscb.set)

    #Posicionando Elementos
    tabela.grid( column=0, row= 0, sticky='nsew')
    vscb.grid( column= 1, row= 0, sticky='ns')
    hscb.grid( column= 0, row= 1, sticky='ew')
    Frame_Direita.grid_rowconfigure( 0, weight= 12)

    #variaveis de posicionamento
    position_coluna = ['nw']
    largura_coluna = [120]

    n = 0 #Contador
    for coluna in tabela_head:
        tabela.heading(coluna, text=coluna.title(), anchor='center')
        tabela.column(coluna, width=105, anchor=position_coluna[n])

        n + 1

    for item in lista:
        tabela.insert('', 'end', values=item)

#chamando a função Mostrar_Tabela
Mostrar_Tabela()

janela.mainloop()

