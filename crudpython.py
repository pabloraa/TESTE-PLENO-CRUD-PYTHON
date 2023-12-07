import mysql.connector

#conexão com o banco mysql, antes deverá criar o banco.
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='30910023',
    database='supermercado',
)

cursor = conexao.cursor()

#CREATE
nome_produto = "Macarrao"
valor = 15.20
comando = f'INSERT INTO produtos (nome_produto,valor) VALUES ("{nome_produto}",{valor})'
cursor.execute(comando) #executa o comando
conexao.commit() #edita o banco de dados
resultado = cursor.fetchall() #ler o bando de dados somente no READ

#READ
comando = f'SELECT * FROM bdyoutube.vendas;'
cursor.execute(comando) #executa o comando
resultado = cursor.fetchall() #ler o bando de dados
print(resultado)

#UPDATE
nome_produto = "todynho"
valor = 6
comando = f'UPDATE bdyoutube.vendas SET valor ={valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando) #executa o comando
conexao.commit() #edita o banco de dados

#DELETE
nome_produto = "chocolate"
valor = 57
comando = f'DELETE FROM bdyoutube.vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando) #executa o comando
conexao.commit() #edita o banco de dados


cursor.close()
conexao.close()