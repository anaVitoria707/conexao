import mysql.connector
from conexao import conexao

def exibir_dados (cursor):
        cursor.execute("SELECT * FROM funcionario")
        resultados = cursor.fetchall()
        print ("\n dados da tabela:")
        for i in resultados:
            print (i)

