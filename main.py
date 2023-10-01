import mysql.connector as mysql
import dotenv as env
from colorama import Fore
import os

# importando os valores do arquivo .env
env.load_dotenv()

# criando a conexao 
conexao = mysql.connect(
    host=os.environ["host"],
    user=os.environ["user"],
    password=os.environ["password"],
    database=os.environ["database"]
)

cursor = conexao.cursor(buffered=True)

# Funções
def exibir_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===============================")
    print(f"{Fore.LIGHTWHITE_EX}       SISTEMA DE AGENDA       {Fore.RESET}")
    print("===============================")
    print(f"1. {Fore.GREEN}Cadastrar{Fore.RESET}")
    print(f"2. {Fore.CYAN}Buscar{Fore.RESET}")
    print(f"3. {Fore.YELLOW}Alterar{Fore.RESET}")
    print(f"4. {Fore.RED}Deletar{Fore.RESET}")
    print("5. Sair")
    print("===============================")

def get_nome(cursor):
    resultado = cursor.fetchall()
    if resultado:
        for linha in resultado:
            nome = linha[0]
    return nome

def executar(comando):
    cursor.execute(comando)
    conexao.commit()

def verifica_id(id):
    if id is None:
        print('\nNão foi encontrado nenhum resultado com essa busca!')
        resposta = input('\nQuer buscar novamente? (s/n) ')
        
        if resposta in 'Nn':
            return 'sair'
        else:
            return 'refazer'

def listar(tabela, id):
    cursor.execute(f'SELECT * FROM {tabela} WHERE codigo = {id}')
    resultado = cursor.fetchall()
    if resultado:
        print('')
        for linha in resultado:
            print(linha[0])
        print('')

def cadastrar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===============================")
    print(f"        {Fore.GREEN}TELA DE CADASTRO{Fore.RESET}        ")
    print("===============================\n")

    while True:
        nome = str(input('Digite o nome na agenda: '))
        executar(f'INSERT INTO agenda (nome) VALUES ("{nome}")')
        codigo = cursor.lastrowid # Recupera o ultimo ID AUTO_INCREMENT

        #Cadastro de Telefone
        resposta = f'\n{Fore.YELLOW}Telefone(s){Fore.RESET}\n'
        print(resposta)
        while not resposta in 'Nn':
            telefone = str(input('Digite o número: '))
            executar(f'INSERT INTO telefone (telefone, codigo) VALUES ("{telefone}", "{codigo}")')
            resposta = str(input('Quer cadastrar outro telefone?(s/n) '))

        #Cadastro de Email
        resposta = f'\n{Fore.MAGENTA}Email(s){Fore.RESET}\n'
        print(resposta)
        while not resposta in 'Nn':
            email = str(input('Digite o email: '))
            executar(f'INSERT INTO email (email, codigo) VALUES ("{email}", "{codigo}")')
            resposta = str(input('Quer cadastrar outro email?(s/n) '))
            
        break

def buscar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===============================")
    print(f"       {Fore.CYAN}TELA DE PESQUISA{Fore.RESET}        ")
    print("===============================\n")

    while True:
        pesquisa = str(input('Selecione por qual tipo irá pesquisar:\n\n1 - Codigo\n2 - Nome\n3 - Telefone\n4 - Email\n\nQual sua escolha? '))           
        
        if pesquisa == '1':
            tipo = str(input('Digite o codigo: '))
            cursor.execute(f'SELECT codigo FROM agenda WHERE codigo = {tipo}')
            
            id = cursor.fetchone()
            resultado = verifica_id(id)
            if resultado == 'sair':
                break
            elif resultado == 'refazer':
                continue
                
            # Pegando o nome da AGENDA
            cursor.execute(f'SELECT nome FROM agenda WHERE codigo = {tipo}') 
            nome = get_nome(cursor)
            print('\nAgenda:', nome)
            print('Codigo:', tipo)

            cursor.execute(f'SELECT * FROM telefone WHERE codigo = "{id[0]}"')
            resultado = cursor.fetchall() 
            if resultado:
                print('\nTelefone(s):\n')
                for linha in resultado:
                    telefone = linha[0]
                    print('- ', telefone)
            else:
                print('\nNão foi encontrado nenhum telefone associado a esta agenda')

            cursor.execute(f'SELECT * FROM email WHERE codigo = "{id[0]}"')
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
            
            id = cursor.fetchone()
            resultado = verifica_id(id)
            if resultado == 'sair':
                break
            elif resultado == 'refazer':
                continue

            # Pegando o nome da AGENDA
            cursor.execute(f'SELECT codigo FROM agenda WHERE nome = "{tipo}"') 
            codigo = get_nome(cursor)
            print('\nAgenda:', tipo)
            print('Codigo:', codigo)
            cursor.execute(f'SELECT * FROM telefone WHERE codigo = "{id[0]}"')

            resultado = cursor.fetchall() 
            if resultado:
                print('\nTelefone(s):\n')
                for linha in resultado:
                    telefone = linha[0]
                    print('- ', telefone)
            else:
                print('\nNão foi encontrado nenhum telefone associado a esta agenda')

            cursor.execute(f'SELECT * FROM email WHERE codigo = "{id[0]}"')
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

            id = cursor.fetchone()
            resultado = verifica_id(id)
            if resultado == 'sair':
                break
            elif resultado == 'refazer':
                continue   

            # Pegando o nome da AGENDA
            cursor.execute(f'SELECT nome FROM agenda WHERE codigo = {id[0]}') 
            nome = get_nome(cursor)
            print('\nAgenda:', nome)
            print('Codigo:', codigo)
             
            cursor.execute(f'SELECT * FROM telefone WHERE codigo = "{id[0]}"')
            resultado = cursor.fetchall() 
            if resultado:
                print('\nTelefone(s):\n')
                for linha in resultado:
                    telefone = linha[0]
                    print('- ', telefone)
            else:
                print('\nNão foi encontrado nenhum telefone associado a esta agenda')

            cursor.execute(f'SELECT * FROM email WHERE codigo = "{id[0]}"')
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

            id = cursor.fetchone()
            resultado = verifica_id(id)
            if resultado == 'sair':
                break
            elif resultado == 'refazer':
                continue

            cursor.execute(f'SELECT nome FROM agenda WHERE codigo = {id[0]}') 
            nome = get_nome(cursor)
            print('\nAgenda:', nome)
            print('Codigo:', codigo)
             
            cursor.execute(f'SELECT * FROM telefone WHERE codigo = "{id[0]}"')
            resultado = cursor.fetchall() 
            if resultado:
                print('\nTelefone(s):\n')
                for linha in resultado:
                    telefone = linha[0]
                    print('- ', telefone)
            else:
                print('\nNão foi encontrado nenhum telefone associado a esta agenda')

            cursor.execute(f'SELECT * FROM email WHERE codigo = "{id[0]}"')
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
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===============================")
    print(f"        {Fore.YELLOW}TELA DE EDIÇÃO{Fore.RESET}         ")
    print("===============================\n")

    while True:
        pesquisa = str(input('Digite o nome da agenda: '))
        cursor.execute(f'SELECT codigo FROM agenda WHERE nome = "{pesquisa}"')
        
        id = cursor.fetchone()
        resultado = verifica_id(id)
        if resultado == 'sair':
            break
        elif resultado == 'refazer':
            continue

        acao = str(input('O que quer fazer?\n\n1 - Editar\n2 - Adicionar\n3 - Excluir\n\nDigite a ação: '))

        if acao == '1':
            tipo = str(input('O que vc quer editar?\n\n1 - Nome\n2 - Email\n3 - Telefone\n\nDigite a ação: '))

            if tipo == '1':
                nome = str(input('Digite o novo nome da agenda: '))
                executar(f'UPDATE agenda SET nome = "{nome}" WHERE codigo = {id[0]}')
                print('\nAgenda editada com sucesso!')

            elif tipo == '2':
                listar('email', id[0])
                email_antigo = str(input('Qual email quer editar? '))
                cursor.execute(f'SELECT codigo FROM email WHERE email  = "{email_antigo}"')
                
                id = cursor.fetchone()
                resultado = verifica_id(id)
                if resultado == 'sair':
                    break
                elif resultado == 'refazer':
                    continue

                email = str(input('Digite o novo email da agenda: '))
                executar(f'UPDATE email SET email = "{email}" WHERE email = "{email_antigo}"')
                print('\nEmail editado com sucesso!')

            elif tipo == '3':
                listar('telefone', id[0])
                telefone_antigo = str(input('Qual telefone quer editar? '))
                cursor.execute(f'SELECT codigo FROM telefone WHERE telefone  = "{telefone_antigo}"')
                
                id = cursor.fetchone()
                resultado = verifica_id(id)
                if resultado == 'sair':
                    break
                elif resultado == 'refazer':
                    continue

                telefone = str(input('Digite o novo telefone da agenda: '))
                executar(f'UPDATE telefone SET telefone = "{telefone}" WHERE telefone = "{telefone_antigo}"')
                print('\nTelefone editado com sucesso!')

        elif acao == '2':
            tipo = str(input('O que vc quer adicionar?\n\n1 - Email\n2 - Telefone\n\nDigite a ação: '))

            if tipo == '1':
                email = str(input('Digite o novo email da agenda: '))
                executar(f'INSERT INTO email (email, codigo) VALUES ("{email}", {id[0]})')
                print('\nEmail adicionado com sucesso!')

            elif tipo == '2':
                telefone = str(input('Digite o novo telefone da agenda: '))
                executar(f'INSERT INTO telefone (telefone, codigo) VALUES ("{telefone}", {id[0]})')
                print('\nTelefone adicionado com sucesso!')

        elif acao == '3':
            tipo = str(input('O que vc quer excluir?\n\n1 - Email\n2 - Telefone\n\nDigite a ação: '))

            if tipo == '1':
                listar('email', id[0])
                email = str(input('Digite o email: '))
                executar(f'DELETE FROM email WHERE email = ("{email}")')
                print('\nEmail deletado com sucesso!')

            elif tipo == '2':
                listar('telefone', id[0])
                telefone = str(input('Digite o telefone: '))
                executar(f'DELETE FROM telefone WHERE telefone = ("{telefone}")')
                print('\nTelefone deletado com sucesso!')

        resposta = str(input('\nQuer editar novamente?(s/n) '))
        if resposta in 'Nn':
            break

def deletar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===============================")
    print(f"       {Fore.RED}TELA DE EXCLUSÃO{Fore.RESET}        ")
    print("===============================\n")

    while True:
        print('Agendas: ')
        cursor.execute(f'SELECT * FROM agenda')
        resultado = cursor.fetchall()
        if resultado:
            print('')
            for linha in resultado:
                print(linha[1])
            print('')

        pesquisa = str(input('Digite o nome da agenda: '))

        cursor.execute(f'SELECT codigo FROM agenda WHERE nome = "{pesquisa}"')
        
        id = cursor.fetchone()
        resultado = verifica_id(id)
        if resultado == 'sair':
            break
        elif resultado == 'refazer':
            continue

        # deletando os telefones com essa chave
        executar(f'DELETE FROM telefone WHERE codigo = {id[0]}')
        # deletando os emails com essa chave
        executar(f'DELETE FROM email WHERE codigo = {id[0]}')
        # deletando a agenda com essa chave
        executar(f'DELETE FROM agenda WHERE codigo = {id[0]}')
        print('\nAgenda deletada com sucesso!')

        resposta = str(input('\nQuer excluir novamente?(s/n) '))
        if resposta in 'Nn':
            break

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