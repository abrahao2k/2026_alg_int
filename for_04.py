# for encadeado (for dentro de for)
# imprimir uma tabela com várias linhas e colunas
import time
for linha in range (6):
    for coluna in range(15):
        print("@", end=" ") # espaço entre colunas
        time.sleep(0.2) # pausa meio segundo
    print("") # próxima linha

