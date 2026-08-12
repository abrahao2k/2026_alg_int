'''6) Escreva um programa que pergunta o valor
de depósito inicial para uma poupança, e a taxa
de rendimento mensal. Apresente o saldo dos
próximos 24 meses, considerando o rendimento sobre 
o saldo atual de cada mês.'''

saldo = float(input("Depósito incial: "))
taxa = float(input("Taxa de rendimento: "))

#1.VALOR INICIAL
mes = 1

#2.TESTE LÓGICO
while mes <= 24:
    rendimento = saldo * (taxa/100)
    saldo += rendimento
    print(f"Mês {mes} - R$ {saldo:.2f}")
    
    #3.INCREMENTO
    mes += 1
    