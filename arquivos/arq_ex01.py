'''1. Escreva o código de um programa que solicita a
digitação de dois valores e exibe a divisão do
primeiro pelo segundo. Use o tratamento de erros
para evitar divisão por zero e valores não numéricos. '''

try:
    v1 = int(input("Valor 1: "))
    v2 = int(input("Valor 2: "))
    print("Divisão =", v1/v2)

except ZeroDivisionError:
    print("O valor 2 não pode ser ZERO.")

except ValueError:
    print("Valor digitado incorretamente.")




