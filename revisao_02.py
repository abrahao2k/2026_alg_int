# 2 LISTAS, FUNÇÕES APPEND, REMOVE, POP, SORT, IN, INDEX,
# CLEAR, SUM, MAX, MIN, COUNT, REVERSE, LEN

lista = []    # list()

lista.append("controle")  # acrescente um item no FINAL da lista
lista.append(6)

lista.insert(0,"palito") # indica posição onde inserir

print(lista)

lista[2] = 65  # atualizar o valor da posição indicada

print(lista[2])

comidas = list(('caldo','batata','sorvete','coxinha'))

comidas.sort() # ordenação crescente

print(comidas)

comidas.reverse() # inverte a lista (de trás para frente)

print(comidas)

comidas.remove('coxinha')  # remover pelo conteúdo

print(comidas)

comidas.pop(0) # remove pela posição

print(comidas)

principal = [ ['caju',5.90], ['manga',3.75] ]  # sublistas

print(principal[0][1]) # acessar um item de sublista

