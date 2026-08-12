'''1) Crie um programa que imprime a tabuada
de multiplicação de um número digitado pelo usuário.
Ex. Usuário digitou "2",
o programa imprime: 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6 ...'''

tabuada = int(input("Imprimir qual tabuada? "))

# 1. VALOR INICIAL
numero = 1

# 2. TESTE LÓGICO
while numero <= 10 :
    
    print(f"{tabuada} x {numero} = {tabuada*numero}")
    
    # 3. INCREMENTO
    #numero = numero + 1
    numero += 1  # forma contraida para soma na variável
