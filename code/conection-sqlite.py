import sqlite3 as sql
import dotenv as env
from colorama import Fore
import os, main

conexao = sql.connect('sqlite.db')
cursor = conexao.cursor()

# Executa o comando para executar
def executar(comando):
    cursor.execute(comando)
    conexao.commit()

cursor.close()
conexao.close()