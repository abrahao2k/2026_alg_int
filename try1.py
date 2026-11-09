try:
    num = int(input("Digite um número:"))
    print("Você digitou:", num)

except ValueError:
    print("ERRO. Digite apenas números.")
