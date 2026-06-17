temp = int(input("Qual a temperatura? "))
# indentação - espaçamento no início da linha
#              para indicar os comandos do desvio
if temp > 25 :
    print("Está calor.")
    print("Esfrie mais, por favor.")

if temp < 18 :
    print("Está frio.")
    print("Esquente um pouco, pela caridade.")
    
if temp >= 18:
    if temp <= 25:
        print("Temperatura agradável.")
        print("Não mude nada.")

print("Fim.")