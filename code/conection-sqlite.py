import sqlite3 as sql
import dotenv as env
from colorama import Fore
import os, functions

conexao = sql.connect('sqlite.db')
cursor = conexao.cursor()

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
        functions.deletar(cursor, conexao)
    elif opcao == "5":
        print("Saindo do programa. Até logo!")
        break
    else:
        input("Opção inválida. Pressione Enter para continuar...")

cursor.close()
conexao.close()