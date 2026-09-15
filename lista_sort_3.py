# ORDENAR SUB-LISTAS
alunos = [ ["joao",72],  ["ana",57], ["elis", 98] ]
               #0            #1            #2

# sort - ordena pela posição 0 (Zero)
alunos.sort()
print(alunos)

# key / lambda - indaca a posição de ordenação
alunos.sort(key=lambda x : x[1])
print(alunos)

alunos.sort(key=lambda x : x[1], reverse=True) # nota decrescente
print(alunos)