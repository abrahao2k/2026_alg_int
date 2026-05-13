# adicionar uma biblioteca no programa
import math

# CALCULAR O FATORIAL ##############################
# 5!  (cinco fatorial)
print( math.factorial(5) )

resultado = math.factorial(3)
print(resultado)

# RAIZ QUADRADA ####################################

print("Raiz de 144 =",  math.sqrt(144) )

# POTÊNCIA #########################################

print( math.pow(2, 4) )   # similar a **  (base, expoente)

# ARREDONDAMENTO PARA CIMA #########################

print( math.ceil( 9.25 ) )  # resulta em 10 (próximo inteiro)

# ARREDONDAMENTO PARA BAIXO ########################

print( math.floor( 17.85 ) ) # resulta 17 (parte inteira)

# ARREDONDAMENTO INDICANDO AS CASAS DECIMAIS ##########

            # numero, casas_decimais
print ( round(3.4187, 2) ) #5,6,7,8,9 - para cima

print ( round(3.4127, 2) ) #0,1,2,3,4 - para baixo

# MMC (MINIMO MULTIPLO COMUM) #########################
      # lower common multiple
print("MMC 10 e 25 = ", math.lcm(10, 25) )

# MDC (MÁXIMO DIVISOR COMUM) ##########################
       #grater common divisor
print("MDC de 10 e 25 = ", math.gcd(10,25) )

# VALOR DE PI #########################################

raio = 3
circ = 2 * math.pi * raio

print("Circunf:", circ )
#print("Circunf:", round(circ,2) )

# VALOR ABSOLUTO ######################################
# valor sem sinal negativo ############################

print( abs(-3) )
print( abs(8) )



