import sqlite3

with sqlite3.connect('artistas.db') as conexao:
    #criar uma conexao com o banco de dados
    sql = conexao.cursor()
    #rodar comeando SQL
    sql.execute('create table banda(nome text, estilo text, membros interger);')
    #exemplo de inserir dados
    sql.execute(
        'insert into banda(nome, estilo, membros) values ("Banda 1","Rock", "3")')
    #exemplo de usar dados da minha aplicação em um comando Sql
    nome = input("Digite o nome da Banda")
    estilo = input("Digite o estilo da Banda")
    qtd_integrantes = int(input("Quantidade de integrantes"))



    sql.execute('insert into banda values(?,?,?)', [
        nome, estilo, qtd_integrantes
    ])
    #Salvando alterações no banco de dados
    conexao.commit()

    #Exibit dados no console Python(terminal)
    bandas = sql.execute('select * from banda;')
    for banda in bandas:
        print(banda)
