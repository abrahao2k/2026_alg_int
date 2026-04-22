''' pergunte o total de gastos de uma pessoa nos meses de
janeiro, fevereiro e março. calcule e mostre a média de gastos
por mês. '''

jan = float(input("Gastos de Janeiro: "))
fev = float(input("Gastos de Fevereiro: "))
mar = float(input("Gastos de Março: "))

media = (jan + fev + mar) / 3

print(f"A média de gastos mensal é R$ {media:.2f}")

