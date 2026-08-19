# while-else, não funciona o else se tem BREAK
# pede para digitar 4 notas, mas
# se a nota for > 100, chama o comando BREAK
soma=0
cont=1 # inicial-2

while cont <= 4: # teste-2
    nota = float(input(f"Digite a nota {cont}: "))
    if nota > 100 : break
    soma += nota
    cont += 1  # increm-2

else:
    print("Média: ", soma/4)