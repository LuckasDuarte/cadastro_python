import sqlite3 as lite

#conectando ao banco
conn = lite.connect('banco.db')


def Inserir_Informacoes(i):
    with conn:                          #Inserir
        cursor = conn.cursor()              
        query = "INSERT INTO formulario (name, email, telefone, data, nivel, sobre) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, i)
        print('Informação Inserida')

def Acessar_Informacoes():
    with conn:
        lista = []
        cursor = conn.cursor()
        query = "SELECT * FROM formulario"      #Acessar Informações
        cursor.execute(query)
        info = cursor.fetchall()
        print(info)

        for i in info:
            lista.append(i)
    return lista
        


def Atualizar_Informacoes(i):
    #Atualizar Informações
    with conn:
        cursor = conn.cursor()
        query = "UPDATE formulario SET name=?, email=?, telefone=?, data=?, nivel=?, sobre=? WHERE id=?"
        cursor.execute(query, i)
        print('Informação Atualizada')

def Deletar_Informacoes(i):
    #Deletar Informações
    with conn:
        cursor = conn.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cursor.execute(query, i)
        print('Informação Deletada')
