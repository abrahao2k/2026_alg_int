# FUNÇÃO COM RETORNO

def quadrado(x):
    total = x * x
    return(total)   # devolve o valor para o programa que chamou
                    # a função
############################################

#quadrado(7) # não mostra nada pq nao tem print
                    
print( quadrado(7) ) # usar com print

result = quadrado(25) # guardar em uma variável

tot = 2 + 8 * 5 + quadrado(5)  # usar a função em um cálculo
print(tot)