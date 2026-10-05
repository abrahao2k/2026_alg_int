'''1. Crie um programa que use um laço for
para solicitar a digitação do nome de 5 alunos.
Guarde-os em uma lista. Após a digitação, exiba a lista.'''

lista = []

for x in range(5):#0,1,2,3,4
    nome=input("Nome do aluno: ")
    lista.append(nome)

print(lista)