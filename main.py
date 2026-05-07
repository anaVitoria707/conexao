import mysql.connector
from conexao import conexao
from cadastroFuncionario3 import inserir_dados
from listarFuncionario3 import exibir_dados


con, cursor = conexao()
inserir_dados(con, cursor)
exibir_dados(cursor)
