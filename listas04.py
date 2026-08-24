# CADASTRO USANDO LISTA E APPEND #
alunos = []  # lista vazia
while True:   # laço infinito
    nome = input("Nome do aluno: ")
    alunos.append(nome) #acrescenta na lista
    resp = input("Cadastrar outro? (s/n) ")
    if resp == "n" : break
print(alunos)