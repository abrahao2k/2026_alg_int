''' usando if / elif / else, faça um programa que
pergunta a idade do usuário e classifica de acordo
com a tabela a seguir:
0 a 11 anos - criança
12 a 17 anos - adolescente
18 a 59 anos - adulto
60 anos ou mais - idoso
valor negativo - idade inválida
'''

idade = int(input("Digite a idade: "))

if    0 <= idade <= 11 : print("Criança")
elif 12 <= idade <= 17 : print("Adolescente")
elif idade>=18 and idade<=59 : print("Adulto")
elif idade >= 60       : print("Idoso")
else                   : print("Idade inválida")
