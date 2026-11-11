arq = open("dados.txt","a")

while True:
    pal = input("Digite uma palavra: ")
    arq.write(pal + "\n")
    print("Gravação realizada.")
    
    res = input("Outra?(s/n) ")
    if res == 'n':
        break

arq.close()