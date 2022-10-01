import sqlite3 as lite

conn = lite.connect('banco.db')

with conn:
    cursor = conn.cursor()
    cursor.execute(""" 
        CREATE TABLE formulario( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            telefone TEXT,
            data DATE,
            nivel TEXT,
            sobre TEXT
        )
    """)
print('Tabela Criada com Sucesso')

