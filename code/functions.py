import os
from colorama import Fore

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

def executar(comando, cursor, conexao):
    cursor.execute(comando)
    conexao.commit()

def get_nome(cursor):
    resultado = cursor.fetchall()
    if resultado:
        for linha in resultado:
            nome = linha[0]
    return nome

def verifica_id(id):
    if id is None:
        print('\nNão foi encontrado nenhum resultado com essa busca!')
        resposta = input('\nQuer buscar novamente? (s/n) ')
        
        if resposta in 'Nn':
            return 'sair'
        else:
            return 'refazer'

def cadastrar(cursor, conexao):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===============================")
    print(f"        {Fore.GREEN}TELA DE CADASTRO{Fore.RESET}        ")
    print("===============================\n")

    while True:
        try:
            nome = str(input('Digite o nome na agenda: '))
            executar(f'INSERT INTO agenda (nome) VALUES ("{nome}")', cursor, conexao)
            codigo = cursor.lastrowid # Recupera o ultimo ID AUTO_INCREMENT

            #Cadastro de Telefone
            resposta = f'\n{Fore.YELLOW}Telefone(s){Fore.RESET}\n'
            print(resposta)
            while not resposta in 'Nn':
                telefone = str(input('Digite o número: '))
                executar(f'INSERT INTO telefone (telefone, codigo) VALUES ("{telefone}", "{codigo}")', cursor, conexao)
                resposta = str(input('Quer cadastrar outro telefone?(s/n) '))

            #Cadastro de Email
            resposta = f'\n{Fore.MAGENTA}Email(s){Fore.RESET}\n'
            print(resposta)
            while not resposta in 'Nn':
                email = str(input('Digite o email: '))
                executar(f'INSERT INTO email (email, codigo) VALUES ("{email}", "{codigo}")', cursor, conexao)
                resposta = str(input('Quer cadastrar outro email?(s/n) '))
            break
        except Exception as e:
            print(f"{Fore.RED}Ocorreu um erro durante o cadastro: {e}{Fore.RESET}")
            conexao.rollback()
            continue

def buscar(cursor, conexao):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===============================")
    print(f"       {Fore.CYAN}TELA DE PESQUISA{Fore.RESET}        ")
    print("===============================\n")

    while True:
        try:
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
        except Exception as e:
            print(f"{Fore.RED}Ocorreu um erro durante o cadastro: {e}{Fore.RESET}")
            conexao.rollback()
            continue

