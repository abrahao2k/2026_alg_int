# JOGO DE ADIVINHAR O NÚMERO SORTEADO
import random  # ativa a biblioteca que sorteia números
sorteado = random.randint(1,100) # sorteia um num entre 1 e 100
#print(sorteado)
pontos = 0  # placar / tentativas
#1.VALOR INICIAL (NÃO PODE SER ENTRE 1 E 100)
digitado = 0
#2.TESTE LÓGICO
while digitado != sorteado :
    #3.INCREMENTO
    digitado = int(input("Dig. número entre 1 e 100: "))
    pontos = pontos + 1  # conta a tentativa
    if digitado == sorteado:
        print("ACERTOU! PARABÉNS!")
        print("Tentativas:", pontos)
    elif digitado < sorteado :
        print("Digitou abaixo. Tente um número MAIOR.")
    elif digitado > sorteado:
        print("Digitou acima. Tente um número MENOR.")