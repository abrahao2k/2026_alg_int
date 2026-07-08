# desvios usando elif
n1 = int(input("Valor1: "))
n2 = int(input("Valor2: "))

print("Escolha:\n1-Soma\n2-Subtr.\n3-Mult.\n4-Divisão")
op = input("Opção? ")

if   op == "1" : print("Soma=", n1 + n2)
elif op == "2" : print("Subtr.=", n1 - n2)
elif op == "3" : print("Mult.=", n1 * n2)
elif op == "4" : print("Divisão=", n1 / n2)
else           : print("Opção inválida.")

