dados = ['tronco','folha','caule','tronco','galho','flor','tronco']
print(dados)
#dados.remove("raiz") # erro se o elemento não existe

item = input("Digite: ")

if item in dados:           # fazer uma busca antes de remover
    dados.remove(item)
else:
    print("Não encontrado.")
    
print(dados)