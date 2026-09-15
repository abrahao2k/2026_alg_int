qtd_alunos = [36, 41, 17, 32, 29, 21]
# MAX - Maior valor de uma lista:
maior = max(qtd_alunos)
print("Turma com mais alunos:", maior )

#nomes=['caio','zico','feliz','luka'] # funciona com nomes
#print(max(nomes))

# MIN - Menor valor de uma lista:
print("Turma com menos alunos:", min(qtd_alunos) )

# DESCOBRIR EM QUAL POSIÇÃO ESTÁ O MENOR VALOR
print("Está na posição:", qtd_alunos.index( min(qtd_alunos) ) )
