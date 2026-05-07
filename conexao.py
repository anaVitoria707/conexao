import mysql.connector

def conexao ():
        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "oficina1"
    )
        print("conectado")
        cursor = con.cursor()
        return con, cursor
        
