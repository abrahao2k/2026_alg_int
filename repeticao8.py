#BREAK - FINALIZA IMEDIATAMENTE A REPETIÇÃO

# um programa que pede a digitação de 10 números
# positivos, mas finaliza se um número negativo
# for digitado

cont = 1
while cont <= 10:
    numero = int(input("Digite um número positivo: "))
    
    if numero < 0 : break
    
    cont += 1  # cont = cont + 1
    
print("FIM")