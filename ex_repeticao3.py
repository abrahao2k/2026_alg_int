'''3) Crie um programa em que o usuário digite 10
números e o programa apresente a soma desses 
números. Dica: use uma variável para acumular a
soma dos números, como no exemplo: soma = 
soma + numero. '''

soma = 0

#1.VALOR INICIAL
contador = 1

#2.TESTE LÓGICO
while contador <= 10:
    numero = int(input("Digite o número a ser somado: "))
    soma += numero  # soma = soma + numero
    
    #3.INCREMENTO
    contador += 1

print("Total = ", soma)
