# Importa a biblioteca 
# Serve para conectar o banco de dados ao python
import mysql.connector 

# Executa uma função da lib que realiza a conexão
conexao = mysql.connector.connect(
# Parâmetro de conexão ao banco de dados 
    host = "localhost",
    user = "root",
    password = "",
    database = "oficina"
)

print("conectado")

# Funçao cursos() da lib
# Serve para manipular os dados de envio para o banco
cursor = conexao.cursor()

# Comandos e valores para envio de dados em SQL
sql = "INSERT INTO funcionario3(nome, salario, contato ) VALUES (%s, %s, %s)"
values = ("pedro", 2000.50, 49999778984 )

cursor.execute(sql, values)
conexao.commit()

cursor.execute("SELECT * FROM funcionario3")
resultado = cursor.fetchall()

for i in resultado:
    print(i)

