lista = ["casa","vela","molho"]  # vazia
print(lista)

lista.insert(0,"legal")     # insere na posição indicada
print(lista)

lista.insert(15,"bobeira")   # se não existe, vai pro final
print(lista)

if "legal" in lista:       # verifica p/ não dar erro
    lista.remove("legal")  # remove por conteúdo

print(lista)

nome = lista.pop()     # permite capturar o valor removido
print("variavel nome=", nome)

print("removendo", lista.pop())

print(lista)

if 0 < len(lista):         # verificar antes de remover
    lista.pop(0)           # remove por posição

print(lista)

#lista.pop()           # sem parâmetro, remove o último