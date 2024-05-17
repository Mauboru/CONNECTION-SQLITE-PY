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
        functions.alterar(cursor, conexao)
    elif opcao == "4":
        functions.deletar()
    elif opcao == "5":
        print("Saindo do programa. Até logo!")
        break
    else:
        input("Opção inválida. Pressione Enter para continuar...")

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