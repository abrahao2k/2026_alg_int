'''Faça um programa que pergunta o preço da gasolina,
depois pergunta quantos litros abasteceu e
calcula e mostra o valor a pagar.'''

preço = float(input("Preço da gasolina: ").replace(',' , '.'))
litros = float(input("Litros abastecidos: ").replace(',' , '.'))

total = preço * litros

print(f"Total a pagar R$ {total:.2f}")

