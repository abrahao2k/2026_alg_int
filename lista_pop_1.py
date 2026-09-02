''' remover um item indicando a POSIÇÃO '''

dados = ['folha','caule','tronco','galho','flor','semente']
           #0       #1      #2       #3     #4      #5
print(dados)

dados.pop(0) # remove o item na posição indicada
print(dados)

posicao = int(input("Qual posição remover? "))

if posicao < len(dados) : dados.pop(posicao) # testa se a posição existe
else: print("posição inválida")
print(dados)