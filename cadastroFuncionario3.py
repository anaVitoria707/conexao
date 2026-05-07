import mysql.connector
from conexao import conexao

def inserir_dados (con, cursor):
        nome = input ("qual seu nome? ")
        salario = int(input("qual seu salário?"))
        contato = int(input("qual seu contato?"))
        sql = "INSERT INTO funcionario3 (nome, salario, contato) VALUES (%s, %s, %s)"
        values = (nome, salario, contato)

        cursor.execute(sql, values)
        
        con.commit()

        print ("inserção feita!")