# pergunta o curso do aluno, se for informática ou eletrotécnica,
# diz que tem vaga de estágio. qualquer outro curso, diz que não tem.

curso = input("Qual o curso? ")

if curso == "informática" or curso == "eletrotécnica":
    print("TEM VAGA de estágio para seu curso.")

else:
    print("NÃO TEM VAGA de estágio nesse curso.")

