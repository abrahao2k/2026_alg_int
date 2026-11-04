# QUESTÃO 13

dados = []

def cadastrar():
    print("*** CADASTRO ***")
    nome = input("Digite o nome: ")
    dados.append(nome)
    print("Cadastrado com sucesso.\n\n")

def listar():
    print("*** LISTAGEM ***")
    if len(dados) == 0 :
        print("Nenhum registro cadastrado.\n\n")
    else:
        dados.sort() # ordenar
        for nome in dados: print(nome)
    print("\n\n")

def excluir():
    print("*** EXCLUSÃO ***")
    if len(dados) == 0:
        print("Nenhum registro cadastrado.\n\n")
    else:
        nome=input("Nome a ser excluído: ")
        if nome in dados:
            dados.remove(nome)
            print("Nome removido.\n\n")
        else:
            print("Nome não existe na lista.\n\n")
            
#######################################################
while True:
    print("*** MENU ***")
    print(" 1-Cadastrar\n 2-Listar\n 3-Excluir\n 4-Sair")
    opcao = int(input("Opção? "))
    if   opcao == 1 : cadastrar()
    elif opcao == 2 : listar()
    elif opcao == 3 : excluir()
    elif opcao == 4 : break
    else : print("Inválido\n\n")