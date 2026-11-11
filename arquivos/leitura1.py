# arquivo .txt na mesma pasta do .py

arq = open("dados.txt", "r", encoding="utf-8")

conteudo = arq.read()

arq.close()

print(conteudo)