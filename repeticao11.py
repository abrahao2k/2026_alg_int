# EXEMPLO USANDO BREAK e CONTINUE

# um laço infinito mostra um menu com as opções: informática,
# eletrotécnica e sair

# para cada opção escolhida, aumente o contador de "votos"

# se digitar uma opção inválida, não conte nada

# se escolher sair, finalize o programa

# no final mostrar quantos "votos" foram aceitos

votos = 0
while True:
    op=int(input("MENU\n1-Informática\n2-Eletro\n3-Sair\nOpção?"))
    
    if op != 1 and op != 2 and op != 3:
        print("Inválido.")
        continue
    
    if op == 3 : break
    
    print("Voto registrado.")
    votos += 1

print("Total de votos =", votos)
