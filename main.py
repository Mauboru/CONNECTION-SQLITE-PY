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
def listar():
    comando = f'SELECT * FROM agenda'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def executar(comando):
    cursor.execute(comando)
    conexao.commit()

#Menu
def exibir_menu():
    limpar()

    print("===============================")
    print("     SISTEMA   DE   AGENDA     ")
    print("===============================")
    print("1. Cadastrar")
    print("2. Buscar")
    print("3. Atualizar Registro")
    print("4. Deletar Registro")
    print("5. Sair")
    print("===============================")

# Função para cadastrar agenda, telefone e email
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

# Função para ler registros
def buscar():
    limpar()
    print("===============================")
    print("    TELA DE BUSCA/PESQUISA     ")
    print("===============================")
    print('')

    while True:
        nome = str(input('Digite o nome da agenda: '))
        cursor.execute(f'SELECT codigo FROM agenda WHERE nome = "{nome}"')
        id_agenda = cursor.fetchone()

        if id_agenda is None:
            print('\nNão foi encontrado nenhuma agenda com esse nome\n')
            resposta = str(input('\nQuer buscar novamente?(s/n) '))
            if resposta in 'Nn':
                break
            else:
                continue

        cursor.execute(f'SELECT * FROM telefone WHERE codigo = "{id_agenda[0]}"')
        resultado = cursor.fetchall()

        print('\nAgenda:', nome)
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

# Função para atualizar um registro
def atualizar_registro():
    limpar
    print("Opção 3 - Atualizar Registro")

# Função para deletar um registro
def deletar_registro():
    limpar
    print("Opção 4 - Deletar Registro")

# Loop principal do programa
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        buscar()
    elif opcao == "3":
        atualizar_registro()
    elif opcao == "4":
        deletar_registro()
    elif opcao == "5":
        print("Saindo do programa. Até logo!")
        break
    else:
        input("Opção inválida. Pressione Enter para continuar...")

#Update
resposta = str(input('Quer editar? '))
while not resposta in 'Nn':
    nome = str(input('Digite o nome na agenda para editar: '))
    novo_nome = str(input('Digite o novo nome: '))
    comando = f'UPDATE agenda SET nome = "{novo_nome}" WHERE nome = "{nome}"'
    cursor.execute(comando)
    conexao.commit()
    resposta = str(input('Quer editar novamente? '))

#Excluir
resposta = str(input('Quer excluir? '))
while not resposta in 'Nn':
    nome = str(input('Digite o nome na agenda para deletar: '))
    comando = f'DELETE FROM agenda WHERE nome = "{nome}"'
    cursor.execute(comando)
    conexao.commit()
    resposta = str(input('Quer excluir novamente? '))

cursor.close()
conexao.close()