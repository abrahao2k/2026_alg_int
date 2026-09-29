comidas = ["bolo","pudim","açaí","sorvete"]

for item in comidas:
    
    if item=="açaí":  break # interrompe o laço 
                        #continue - pula pro próximo elemento
    print(f"Eu gosto de {item}.")

else:   # executa se passar por todos os itens
    print("Comi tudo.")  # se charmar break não executa else