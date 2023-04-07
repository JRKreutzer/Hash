import hashlib # Importa a biblioteca necessária para fazer o SHA512
import re # Importa a biblioteca necessária para fazer as pesquisas de validação das senhas e email

#Função para data e hora

from datetime import datetime # Importa a biblioteca para imprimir o tempo

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y")

print(data_e_hora_em_texto)

# Função para criar hash da senha

def criar_hash(senha):
    return hashlib.sha512(senha.encode('utf-8')).hexdigest() # Converte uma senha em hash

# Iniciando arquivo com data de acesso

with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{'Login realizado'}, {'dia'}, {data_e_hora_atuais}\n") 

# Função para validar senha

def confereSenha(senha):

    testeSenha = True;
    
    if (len(senha)<8): #Verifica se a senha é menor que 8 digitos
        print("Password Não válido, senha menor que 8 dígitos!")
        testeSenha = False;
    if not re.search("[a-z]", senha): # Verifica se a senha tem letras minúsculas
        print("Password Não válido, senha sem letra minúscula.")
        testeSenha = False;
    if not re.search("[A-Z]", senha): # Verifica se a senha tem letras Maiúsculas
        print("Password Não válido, senha sem letra maíscula.")
        testeSenha = False;
    if not re.search("[0-9]", senha): # Verifica se a senha tem digitos
        print("Password Não válido, senha sem números.")
        testeSenha = False;
    if not re.search("[#$%^&*()[/\\]]", senha): # Verifica se a senha tem caracteres especiais
        print("Password Não válido, senha sem caractéres [#$%^&*()[/\\]].")
        testeSenha = False;
    if re.search("\s", senha): # Verifica se a senha está vazia
        print("Password Não válido")
        testeSenha = False;
    if (len(senha)>36): # Verifica se a senha é maior que 36 digitos
        print("Password Não válido, senha maior que 36 dígitos.")
        testeSenha = False;
    if testeSenha == True: 
        print("Password Válido!") 

    return testeSenha; # Retorna Verdadeiro se a senha atende a todos os requisitos ou falso se algum requisito não foi atendido

# Função para validar email

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' # Define um padrão para email
      
def confereEmail(email):  

    testeEmail = True;
    if(re.search(regex,email)):  # Verifica se o email segue o padrão definido
        print("E-mail válido!")  
          
    else:  
        print("E-mail inválido!")
        testeEmail = False;

    return testeEmail;

# Função para cadastrar novo usuário

def cadastrar():

    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    validadorSenha = confereSenha(senha); # Verifica se a senha é válida 
    validadorEmail = confereEmail(email); # Verifica se o email é válido
    
    if (validadorSenha == True and validadorEmail == True): # Caso o email e a senha forem válido cria um hash da senha
        # Criar hash da senha
        hash_senha = criar_hash(senha)    
    
        with open("usuarios.txt", "r") as arquivo: # Abrir o arquivo usuarios.txt em formato de leitura
            for linha in arquivo: # Para cada linha do aquivo verificar se o email que se deseja cadastrar já não foi cadastrado antes
                nome_salvo, email_salvo, hash_senha_salvo = linha.strip().split(",")
                if email == email_salvo:
                    print(f"Erro! Email já cadastrado!") # Caso tenha sido envia mensagem de erro
                    return
        # Salvar informações do usuário em arquivo
            else:
                with open("usuarios.txt", "a") as arquivo: # Senão abre o aquivo em formate de append (adicionar) e salva uma nova linha no arquivo com nome, email e hash
                    arquivo.write(f"{nome.strip()},{email},{hash_senha}\n")
        
                    print("Usuário cadastrado com sucesso!")
    else:
        print("Falha ao cadastrar!")
        
# Função para fazer login

def fazer_login():

    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    # Criar hash da senha

    hash_senha = criar_hash(senha) # Transforma a senha digitada em hash para fazer a comparação com a senha salva no arquivo

    with open("usuarios.txt", "r") as arquivo: # Abrir o arquivo usuarios.txt em formato de leitura
        for linha in arquivo: # Para cada linha do aquivo verificar se o email e senha digitada são iguais
            nome_salvo, email_salvo, hash_senha_salvo = linha.strip().split(",")
            if email == email_salvo and hash_senha == hash_senha_salvo: # Se encontrar uma combinação válida
                print(f"Bem-vindo, {nome_salvo}!") # Imprimi uma mensagem dando boas vindas ao usuário encontrado
                return
    
    print("E-mail ou senha inválidos.")

# Menu principal

while True:
    print("1 - Cadastrar novo usuário")
    print("2 - Fazer login")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar() # Chama a função para fazer o cadastro
    elif opcao == "2":
        fazer_login() # Chama a função para fazer login
    elif opcao == "3":
        break # Finaliza o programa
    else:
        print("Opção inválida. Tente novamente.")
