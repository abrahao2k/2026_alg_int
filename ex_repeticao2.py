'''2) Modifique o programa anterior de maneira que
o usuário também digite o início e o fim da 
tabuada, ao invés de ir de 1 a 10.
Ex. Tabuada de: 2, início: 5, fim: 12.
Vai imprimir: 2 x 5 = 10, 2 x 6 
= 12, ... 2 x 12 = 24. '''

tabuada = int(input("Qual tabuada imprimir? "))
atual   = int(input("Valor inicial: ")) # 1.VALOR INICIAL
final   = int(input("Valor final: "))

#2.TESTE LÓGICO
while atual <= final:
    print(f"{tabuada} x {atual} = {tabuada*atual}")
    #3.INCREMENTO
    atual += 1