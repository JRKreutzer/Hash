import time # Importa a biblioteca tempo para calcular o tempo necessário para realizar uma operação

# Função que recebe dois arquivos .txt e compara cada linha para encontrar hashs iguais

def comparador(nome1, nome2): # Função que recebe dois arquivos .txt e compara cada linha para encontrar hashs iguais

    with open(nome1, "r") as arquivo2: # Abrir o arquivo onde os usuários estão salvos
        for linha in arquivo2: # Para cada linha do arquivo com os usuários
            nome, email_salvo, hash_senha_salvo = linha.strip().split(",") # Tranforma a linha em um array, cada elemento dentro do array é separado por vírgula
            with open(nome2, "r") as arquivo: # Abrir o arquivo onde as senhas geradas estão salvas
                 for linha2 in arquivo: # Para cada linha do aquivo com as senhas
                    senha,hash_senha_salvo_2 = linha2.strip().split(",") # Tranforma a linha em um array, cada elemento dentro do array é separado por vírgula
                    
                    if hash_senha_salvo_2 == hash_senha_salvo: # Verifica se o hash salvo na linha usuário é igual ao hash da linha senhas geradas
                        print("Senha encontrada!")
                        print("Email:", email_salvo, "Senha:", senha) # Imprimi na tela o Email salvo no arquivo dos usuarios e a senha salva no arquivo senhas geradas

# Menu principal

while True:
    print("Bem vindo ao gerador de senhas!")
    print("Digite 1 para comparar as senhas.")
    print("Digite 2 para sair.")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome2 = input("Digite o nome do arquivo do dicionário de senhas (Lembre de digitar a extensão .txt no fim):")
        nome1 = input("Digite o nome do arquivo com os dados do cadastro salvo (Lembre de digitar a extensão .txt no fim):")
        inicio = time.time() # Função para marcar o início do processo de geração de senhas
        comparador(nome1, nome2) # Compara as linhas do arquivo nome1 com as linhas do arquivo nome2
        fim = time.time() # Função para marcar o fim do processo de geração de senhas
        tempo_total = fim - inicio # Calculo para o tempo total do processo de geração de senhas
        print("Tempo de execução: {:.2f} segundos".format(tempo_total)) # Imprimi quanto tempo levou para gerar as senhas
    elif opcao == "2":
        break # Finaliza o programa
    else:
        print("Opção inválida. Tente novamente.")
