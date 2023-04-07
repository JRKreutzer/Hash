import random # Importa a biblioteca para escolher numeros, letras e caracteres aleatórios
import string # Importa a biblioteca que contém um conjunto de strings, maiúsculas, minúsculas, digitos...
import hashlib # Importa a biblioteca necessária para gerar o SHA512
import time # Importa a biblioteca tempo para calcular o tempo necessário para realizar uma operação

punctuation = '#$%^&*()[/\\]' # Define os caracteres especiais aceitos na senha

# Função para criar hash da senha

def criar_hash(senha):
    return hashlib.sha512(senha.encode('utf-8')).hexdigest() # Converte uma senha em hash

# Função para gerar uma senha, recebe o tamanho que a senha terá

def gerar_senha(tamanho):
    while True:
        senha = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + punctuation, k=tamanho)) # Gera uma senha aleatória com 8 caracteres contendo pelo menos uma letra minúscula, uma maiúscula, um número e um caractere especial
        if (any(c.islower() for c in senha) # Procura uma letra minúscula dentro da senha
            and any(c.isupper() for c in senha) # Procura uma letra maiúscula dentro da senha
            and any(c.isdigit() for c in senha) # Procura um digito dentro da senha
            and any(c in punctuation for c in senha)): # Procura um caractere especial dentro da senha
            return senha # Caso encontre todos retorna a senha

# Função para salvar as senhas, recebe o nome do arquivo que será salvo, o tamanho da senha e a quantidade de senhas

def salvar_senhas(arquivo, num_senhas, tamanho):
    with open(arquivo, 'a') as f: # # Abrir o arquivo em formato de append (adicionar) 
        senhas = set() # Para que não se tenha senhas repetidas
        i = 0 
        while i < num_senhas: # Enquanto i for menor que o número de senhas desejadas
            senha = gerar_senha(tamanho) # Cria uma senha com a função gerar_senha 
            hash_senha = criar_hash(senha) # Calcula o hash dessa senha
            f.write(f"{senha},{hash_senha}\n") # Escreve essa senha no arquivo
            i += 1

# Função para gerar todas as senhas desejadas

def gerar():
    
    y = int(input("Quantos digitos a senha ter? "))
    while y < 8: # Caso o usuário digite um valor menor que 8, um novo valor será solicitado
        y = int(input("Senha muito pequena! Digite ao menos 8 digitos:"))
    x = int(input("Quantos senhas devem ser geradas? ")) 
    nome = input('Digite o nome do arquivo que será salvo("lembre de digitar .txt no final"):')
    inicio = time.time() # Função para marcar o início do processo de geração de senhas
    salvar_senhas(nome, x, y) # Gera e salva x senhas com y tamanho no arquivo nome.txt
    fim = time.time() # Função para marcar o fim do processo de geração de senhas
    tempo_total = fim - inicio # Calculo para o tempo total do processo de geração de senhas
    print("Tempo de execução: {:.2f} segundos".format(tempo_total)) # Imprimi quanto tempo levou para gerar as senhas


# Menu principal

while True:
    print("Bem vindo ao gerador de senhas!")
    print("Digite 1 para gerar senhas.")
    print("Digite 2 para sair.")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        gerar() # Função para gerar todas as senhas desejadas
    elif opcao == "2":
        break # Finaliza o programa
    else:
        print("Opção inválida. Tente novamente.")

