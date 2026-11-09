try:
    print(legal)
    n1=int(input("Primeiro número: "))
    n2=int(input("Segundo número: "))
    print("Resultado =", n1/n2)

except ZeroDivisionError:
    print("O segundo número não pode ser zero.")

except (ValueError, TypeError):
    print("Erro ao ler os valores. Verifique.")

except: # captura qualquer erro não citado anteriormente
    print("Erro desconhecido.")
    raise # mostra o erro após a execução do programa

finally:
    print("Até a próxima!")