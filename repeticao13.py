# LAÇOS ENCADEADOS
# uma repetição controla se quer cadastrar um aluno
# dentro dele outro laço controla a digitação de 4 notas
# para calcular a média

resp = "s"         # inicial-1
while resp == "s": # teste-1
    
    soma=0
    cont=1 # inicial-2
    while cont <= 4: # teste-2
        nota = float(input(f"Digite a nota {cont}: "))
        soma += nota
        cont += 1  # increm-2
    print("Média: ", soma/4)
    
    resp = input("Cadastrar outro? (s/n) ") # increm-1
    
else:
    print("Obrigado por usar esse programa. :) ")
    