import mysql.connector as mysql
import dotenv as env
from colorama import Fore
import os, functions

# importando os valores do arquivo .env
env.load_dotenv()

# criando a conexao por MySQL
conexao = mysql.connect(
    host=os.environ["host"],
    user=os.environ["user"],
    password=os.environ["password"],
    database=os.environ["database"]
)
cursor = conexao.cursor(buffered=True)

while True:
    functions.exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        functions.cadastrar(cursor, conexao)
    elif opcao == "2":
        functions.buscar(cursor, conexao)
    elif opcao == "3":
        functions.alterar()
    elif opcao == "4":
        functions.deletar()
    elif opcao == "5":
        print("Saindo do programa. Até logo!")
        break
    else:
        input("Opção inválida. Pressione Enter para continuar...")

# def listar(tabela, id):
#     cursor.execute(f'SELECT * FROM {tabela} WHERE codigo = {id}')
#     resultado = cursor.fetchall()
#     if resultado:
#         print('')
#         for linha in resultado:
#             print(linha[0])
#         print('')

# def alterar():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("===============================")
#     print(f"        {Fore.YELLOW}TELA DE EDIÇÃO{Fore.RESET}         ")
#     print("===============================\n")

#     while True:
#         pesquisa = str(input('Digite o nome da agenda: '))
#         cursor.execute(f'SELECT codigo FROM agenda WHERE nome = "{pesquisa}"')
        
#         id = cursor.fetchone()
#         resultado = verifica_id(id)
#         if resultado == 'sair':
#             break
#         elif resultado == 'refazer':
#             continue

#         acao = str(input('O que quer fazer?\n\n1 - Editar\n2 - Adicionar\n3 - Excluir\n\nDigite a ação: '))

#         if acao == '1':
#             tipo = str(input('O que vc quer editar?\n\n1 - Nome\n2 - Email\n3 - Telefone\n\nDigite a ação: '))

#             if tipo == '1':
#                 nome = str(input('Digite o novo nome da agenda: '))
#                 executar(f'UPDATE agenda SET nome = "{nome}" WHERE codigo = {id[0]}')
#                 print('\nAgenda editada com sucesso!')

#             elif tipo == '2':
#                 listar('email', id[0])
#                 email_antigo = str(input('Qual email quer editar? '))
#                 cursor.execute(f'SELECT codigo FROM email WHERE email  = "{email_antigo}"')
                
#                 id = cursor.fetchone()
#                 resultado = verifica_id(id)
#                 if resultado == 'sair':
#                     break
#                 elif resultado == 'refazer':
#                     continue

#                 email = str(input('Digite o novo email da agenda: '))
#                 executar(f'UPDATE email SET email = "{email}" WHERE email = "{email_antigo}"')
#                 print('\nEmail editado com sucesso!')

#             elif tipo == '3':
#                 listar('telefone', id[0])
#                 telefone_antigo = str(input('Qual telefone quer editar? '))
#                 cursor.execute(f'SELECT codigo FROM telefone WHERE telefone  = "{telefone_antigo}"')
                
#                 id = cursor.fetchone()
#                 resultado = verifica_id(id)
#                 if resultado == 'sair':
#                     break
#                 elif resultado == 'refazer':
#                     continue

#                 telefone = str(input('Digite o novo telefone da agenda: '))
#                 executar(f'UPDATE telefone SET telefone = "{telefone}" WHERE telefone = "{telefone_antigo}"')
#                 print('\nTelefone editado com sucesso!')

#         elif acao == '2':
#             tipo = str(input('O que vc quer adicionar?\n\n1 - Email\n2 - Telefone\n\nDigite a ação: '))

#             if tipo == '1':
#                 email = str(input('Digite o novo email da agenda: '))
#                 executar(f'INSERT INTO email (email, codigo) VALUES ("{email}", {id[0]})')
#                 print('\nEmail adicionado com sucesso!')

#             elif tipo == '2':
#                 telefone = str(input('Digite o novo telefone da agenda: '))
#                 executar(f'INSERT INTO telefone (telefone, codigo) VALUES ("{telefone}", {id[0]})')
#                 print('\nTelefone adicionado com sucesso!')

#         elif acao == '3':
#             tipo = str(input('O que vc quer excluir?\n\n1 - Email\n2 - Telefone\n\nDigite a ação: '))

#             if tipo == '1':
#                 listar('email', id[0])
#                 email = str(input('Digite o email: '))
#                 executar(f'DELETE FROM email WHERE email = ("{email}")')
#                 print('\nEmail deletado com sucesso!')

#             elif tipo == '2':
#                 listar('telefone', id[0])
#                 telefone = str(input('Digite o telefone: '))
#                 executar(f'DELETE FROM telefone WHERE telefone = ("{telefone}")')
#                 print('\nTelefone deletado com sucesso!')

#         resposta = str(input('\nQuer editar novamente?(s/n) '))
#         if resposta in 'Nn':
#             break

# def deletar():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("===============================")
#     print(f"       {Fore.RED}TELA DE EXCLUSÃO{Fore.RESET}        ")
#     print("===============================\n")

#     while True:
#         print('Agendas: ')
#         cursor.execute(f'SELECT * FROM agenda')
#         resultado = cursor.fetchall()
#         if resultado:
#             print('')
#             for linha in resultado:
#                 print(linha[1])
#             print('')

#         pesquisa = str(input('Digite o nome da agenda: '))

#         cursor.execute(f'SELECT codigo FROM agenda WHERE nome = "{pesquisa}"')
        
#         id = cursor.fetchone()
#         resultado = verifica_id(id)
#         if resultado == 'sair':
#             break
#         elif resultado == 'refazer':
#             continue

#         # deletando os telefones com essa chave
#         executar(f'DELETE FROM telefone WHERE codigo = {id[0]}')
#         # deletando os emails com essa chave
#         executar(f'DELETE FROM email WHERE codigo = {id[0]}')
#         # deletando a agenda com essa chave
#         executar(f'DELETE FROM agenda WHERE codigo = {id[0]}')
#         print('\nAgenda deletada com sucesso!')

#         resposta = str(input('\nQuer excluir novamente?(s/n) '))
#         if resposta in 'Nn':
#             break


cursor.close()
conexao.close()