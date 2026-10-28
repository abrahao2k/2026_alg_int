# GERADOR DE SENHA
import random

def gerarSenha(p1, p2):
    senha = p1[0] + p1[len(p1)-1]
    senha += str(random.randint(1000,9999))
    senha += p2[0] + p2[len(p2)-1]
    print("A senha gerada foi:", senha)
############################################
palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")
gerarSenha(palavra1, palavra2)