import mysql.connector as mysql
from dotenv import load_dotenv
import os

# importando os valores do arquivo .env
load_dotenv()

# criando a conexao 
conexao = mysql.connect(
    host=os.environ["host"],
    user=os.environ["user"],
    password=os.environ["password"],
    database=os.environ["database"]
)

cursor = conexao.cursor(buffered=True)

#Funções
def get_nome(cursor):
    resultado = cursor.fetchall()
    if resultado:
        for linha in resultado:
            nome = linha[0]
    return nome

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def executar(comando):
    cursor.execute(comando)
    conexao.commit()

def exibir_menu():
    limpar()

    print("===============================")
    print("     SISTEMA   DE   AGENDA     ")
    print("===============================")
    print("1. Cadastrar")
    print("2. Buscar")
    print("3. Alterar")
    print("4. Deletar Registro")
    print("5. Sair")
    print("===============================")

def cadastrar():
    limpar()
    print("===============================")
    print("    CADASTRO DE NOVA AGENDA     ")
    print("===============================")
    print('')

    while True:
        # Cadastro do nome da agenda
        nome = str(input('Digite o nome na agenda: '))
        comando = f'INSERT INTO agenda (nome) VALUES ("{nome}")'
        executar(comando)
        codigo = cursor.lastrowid # Recupera o ultimo ID AUTO_INCREMENT

        #Cadastro de Telefone
        resposta_interna = '\nTelefone(s)\n'
        print(resposta_interna)
        while not resposta_interna in 'Nn':
            telefone = str(input('Digite o número: '))
            comando = f'INSERT INTO telefone (telefone, codigo) VALUES ("{telefone}", "{codigo}")'
            executar(comando)
            resposta_interna = str(input('Quer cadastrar outro telefone?(s/n) '))

        #Cadastro de Email
        resposta_interna = '\nEmail(s)\n'
        print(resposta_interna)
        while not resposta_interna in 'Nn':
            email = str(input('Digite o email: '))
            comando = f'INSERT INTO email (email, codigo) VALUES ("{email}", "{codigo}")'
            executar(comando)
            resposta_interna = str(input('Quer cadastrar outro email?(s/n) '))
            
        break

def buscar():
    limpar()
    print("===============================")
    print("    TELA DE BUSCA/PESQUISA     ")
    print("===============================")
    print('')

    while True:
        pesquisa = str(input('Selecione qual tipo irá pesquisar:\n\n1 - Codigo\n2 - Nome\n3 - Telefone\n4 - Email\n\nQual sua escolha? '))           
        if pesquisa == '1':
            tipo = str(input('Digite o codigo: '))
            cursor.execute(f'SELECT codigo FROM agenda WHERE codigo = {tipo}')
            id_agenda = cursor.fetchone() #verificando se existe algo com esse valor
            if id_agenda is None:
                print('\nNão foi encontrado nenhuma resultado com essa busca!\n')
                resposta = str(input('\nQuer buscar novamente?(s/n) '))
                if resposta in 'Nn':
                    break
                else:
                    continue     

            # Pegando o nome da AGENDA
            cursor.execute(f'SELECT nome FROM agenda WHERE codigo = {tipo}') 
            nome = get_nome(cursor)
            print('\nAgenda:', nome)
             
            cursor.execute(f'SELECT * FROM telefone WHERE codigo = "{id_agenda[0]}"')
            resultado = cursor.fetchall() 

            if resultado:
                print('\nTelefone(s):\n')
                for linha in resultado:
                    telefone = linha[0]
                    print('- ', telefone)
            else:
                print('\nNão foi encontrado nenhum telefone associado a esta agenda')

            cursor.execute(f'SELECT * FROM email WHERE codigo = "{id_agenda[0]}"')
            resultado = cursor.fetchall()

            if resultado:
                print('\nEmail(s):\n')
                for linha in resultado:
                    email = linha[0]
                    print('- ', email)
            else:
                print('\nNão foi encontrado nenhum email associado a esta agenda')

        elif pesquisa == '2':
            tipo = str(input('Digite o nome: '))
            cursor.execute(f'SELECT codigo FROM agenda WHERE nome = "{tipo}"')
            
            id_agenda = cursor.fetchone()
            if id_agenda is None:
                print('\nNão foi encontrado nenhuma resultado com essa busca!\n')
                resposta = str(input('\nQuer buscar novamente?(s/n) '))
                if resposta in 'Nn':
                    break
                else:
                    continue  

            # Pegando o nome da AGENDA
            cursor.execute(f'SELECT codigo FROM agenda WHERE nome = "{tipo}"') 
            codigo = get_nome(cursor)
            print('\nAgenda:', tipo, ' / codigo(', codigo,')')
            cursor.execute(f'SELECT * FROM telefone WHERE codigo = "{id_agenda[0]}"')
            resultado = cursor.fetchall() 

            if resultado:
                print('\nTelefone(s):\n')
                for linha in resultado:
                    telefone = linha[0]
                    print('- ', telefone)
            else:
                print('\nNão foi encontrado nenhum telefone associado a esta agenda')

            cursor.execute(f'SELECT * FROM email WHERE codigo = "{id_agenda[0]}"')
            resultado = cursor.fetchall()

            if resultado:
                print('\nEmail(s):\n')
                for linha in resultado:
                    email = linha[0]
                    print('- ', email)
            else:
                print('\nNão foi encontrado nenhum email associado a esta agenda') 

        elif pesquisa == '3':
            tipo = str(input('Digite o telefone: '))
            cursor.execute(f'SELECT codigo FROM telefone WHERE telefone  = {tipo}')
            id_agenda = cursor.fetchone() #verificando se existe algo com esse valor
            if id_agenda is None:
                print('\nNão foi encontrado nenhuma resultado com essa busca!\n')
                resposta = str(input('\nQuer buscar novamente?(s/n) '))
                if resposta in 'Nn':
                    break
                else:
                    continue     

            # Pegando o nome da AGENDA
            cursor.execute(f'SELECT nome FROM agenda WHERE codigo = {id_agenda[0]}') 
            nome = get_nome(cursor)
            print('\nAgenda:', nome)
             
            cursor.execute(f'SELECT * FROM telefone WHERE codigo = "{id_agenda[0]}"')
            resultado = cursor.fetchall() 

            if resultado:
                print('\nTelefone(s):\n')
                for linha in resultado:
                    telefone = linha[0]
                    print('- ', telefone)
            else:
                print('\nNão foi encontrado nenhum telefone associado a esta agenda')

            cursor.execute(f'SELECT * FROM email WHERE codigo = "{id_agenda[0]}"')
            resultado = cursor.fetchall()

            if resultado:
                print('\nEmail(s):\n')
                for linha in resultado:
                    email = linha[0]
                    print('- ', email)
            else:
                print('\nNão foi encontrado nenhum email associado a esta agenda')
        
        elif pesquisa == '4':
            tipo = str(input('Digite o email: '))
            cursor.execute(f'SELECT codigo FROM email WHERE email  = "{tipo}"')
            id_agenda = cursor.fetchone() #verificando se existe algo com esse valor
            if id_agenda is None:
                print('\nNão foi encontrado nenhuma resultado com essa busca!\n')
                resposta = str(input('\nQuer buscar novamente?(s/n) '))
                if resposta in 'Nn':
                    break
                else:
                    continue     

            # Pegando o nome da AGENDA
            cursor.execute(f'SELECT nome FROM agenda WHERE codigo = {id_agenda[0]}') 
            nome = get_nome(cursor)
            print('\nAgenda:', nome)
             
            cursor.execute(f'SELECT * FROM telefone WHERE codigo = "{id_agenda[0]}"')
            resultado = cursor.fetchall() 

            if resultado:
                print('\nTelefone(s):\n')
                for linha in resultado:
                    telefone = linha[0]
                    print('- ', telefone)
            else:
                print('\nNão foi encontrado nenhum telefone associado a esta agenda')

            cursor.execute(f'SELECT * FROM email WHERE codigo = "{id_agenda[0]}"')
            resultado = cursor.fetchall()

            if resultado:
                print('\nEmail(s):\n')
                for linha in resultado:
                    email = linha[0]
                    print('- ', email)
            else:
                print('\nNão foi encontrado nenhum email associado a esta agenda')

        resposta = str(input('\nQuer buscar novamente?(s/n) '))
        if resposta in 'Nn':
            break

def alterar():
    limpar()
    print("===============================")
    print("       TELA  DE  EDIÇÃO        ")
    print("===============================")
    print('')

    while True:
        pesquisa = str(input('Digite o nome da agenda: '))

        cursor.execute(f'SELECT codigo FROM agenda WHERE nome = "{pesquisa}"')
        id_agenda = cursor.fetchone()
        if id_agenda is None:
            print('\nNão foi encontrado nenhuma resultado com essa busca!')
            resposta = str(input('\nQuer buscar novamente?(s/n) '))
            if resposta in 'Nn':
                break
            else:
                continue 

        acao = str(input('O que quer fazer?\n\n1 - Editar\n2 - Adicionar\n3 - Excluir\n\nDigite a ação: '))
        if acao == '1':
            tipo = str(input('O que vc quer editar?\n\n1 - Nome\n2 - Email\n3 - Telefone\n\nDigite a ação: '))

            if tipo == '1':
                nome = str(input('Digite o novo nome da agenda: '))
                executar(f'UPDATE agenda SET nome = "{nome}" WHERE codigo = {id_agenda[0]}')
                print('\nAgenda editada com sucesso!')

            elif tipo == '2':
                #listar os emails
                email_antigo = str(input('Qual email quer editar? '))
                cursor.execute(f'SELECT codigo FROM email WHERE email  = "{email_antigo}"')
                id_agenda = cursor.fetchone()
                if id_agenda is None:
                    print('\nNão foi encontrado nenhuma resultado com essa busca!')
                    resposta = str(input('\nQuer buscar novamente?(s/n) '))
                    if resposta in 'Nn':
                        break
                    else:
                        continue
                email = str(input('Digite o novo email da agenda: '))
                executar(f'UPDATE email SET email = "{email}" WHERE email = "{email_antigo}"')
                print('\nEmail editado com sucesso!')

            elif tipo == '3':
                #listar os telefones
                telefone_antigo = str(input('Qual telefone quer editar? '))
                cursor.execute(f'SELECT codigo FROM telefone WHERE telefone  = "{telefone_antigo}"')
                id_agenda = cursor.fetchone()
                if id_agenda is None:
                    print('\nNão foi encontrado nenhuma resultado com essa busca!')
                    resposta = str(input('\nQuer buscar novamente?(s/n) '))
                    if resposta in 'Nn':
                        break
                    else:
                        continue
                telefone = str(input('Digite o novo telefone da agenda: '))
                executar(f'UPDATE telefone SET telefone = "{telefone}" WHERE telefone = "{telefone_antigo}"')
                print('\nTelefone editado com sucesso!')

        elif acao == '2':
            tipo = str(input('O que vc quer adicionar?\n\n1 - Email\n2 - Telefone\n\nDigite a ação: '))

            if tipo == '1':
                email = str(input('Digite o novo email da agenda: '))
                executar(f'INSERT INTO email (email, codigo) VALUES ("{email}", {id_agenda[0]})')
                print('\nEmail adicionado com sucesso!')

            elif tipo == '2':
                telefone = str(input('Digite o novo telefone da agenda: '))
                executar(f'INSERT INTO telefone (telefone, codigo) VALUES ("{telefone}", {id_agenda[0]})')
                print('\nTelefone adicionado com sucesso!')

        elif acao == '3':
            tipo = str(input('O que vc quer excluir?\n\n1 - Email\n2 - Telefone\n\nDigite a ação: '))

            if tipo == '1':
                # listar emails
                email = str(input('Digite o email: '))
                executar(f'DELETE FROM email WHERE email = ("{email}")')
                print('\nEmail deletado com sucesso!')

            elif tipo == '2':
                # listar telefones
                telefone = str(input('Digite o telefone: '))
                executar(f'DELETE FROM telefone WHERE telefone = ("{telefone}")')
                print('\nTelefone deletado com sucesso!')

        resposta = str(input('\nQuer editar novamente?(s/n) '))
        if resposta in 'Nn':
            break

def deletar():
    limpar()
    print("===============================")
    print("      TELA  DE  EXCLUSÃO       ")
    print("===============================")
    print('')

# Loop principal do programa
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        buscar()
    elif opcao == "3":
        alterar()
    elif opcao == "4":
        deletar()
    elif opcao == "5":
        print("Saindo do programa. Até logo!")
        break
    else:
        input("Opção inválida. Pressione Enter para continuar...")
        
cursor.close()
conexao.close()