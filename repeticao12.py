# LAÇOS ENCADEADOS (WHILE DENTRO DE WHILE)

# imprimir as tabuadas de 1 até 10

tab = 1  # inicial-1
while tab <= 10:  # teste-1

    num = 1 # inicial-2
    while num <= 10:  # teste-2
        print(f"{tab} x {num} = {tab*num}")
        num += 1  # incremento-2
    
    tab += 1
    
