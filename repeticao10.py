# CONTINUE - reinicia a repetição sem executar os
# comandos abaixo do continue

cont = 1
while cont <= 10:
    numero = int(input(f"Digite um número positivo {cont}: "))
    
    if numero < 0 : continue  # SOBE PRA LINHA DO while
    
    cont += 1

print("FIM")