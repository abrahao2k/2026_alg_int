# estacionamento, até 10 min = grátis, +q 10 min: moto 5,00 / carro 10,00

tempo = int(input("Tempo (em minutos)? "))
veiculo = input("Veículo (carro/moto)? ")

if tempo <= 10 :
    print("Tarifa: GRÁTIS")

else:
    
    if veiculo == "moto" :
        print("Tarifa: R$ 5,00")
    
    else:
        print("Tarifa: R$ 10,00")

