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

def cadastrar(cursor, conexao):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===============================")
    print(f"        {Fore.GREEN}TELA DE CADASTRO{Fore.RESET}        ")
    print("===============================\n")

    while True:
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

