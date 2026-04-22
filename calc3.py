'''faça um programa que converte REAIS para DÓLAR.
pergunte o valor em Reais, pergunte a cotação do Dólar,
calcule e mostre o resultado da conversão '''

reais = float(input("Valor em Reais: "))     # .replace(',', '.')
cotacao = float(input("Cotação do Dólar: ")) # muda , por .

total = reais / cotacao

print(f"Você tem Us$ {total:.2f} Dólares.")