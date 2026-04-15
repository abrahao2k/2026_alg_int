'''
Faça um programa que pergunta os detalhes do endereço
do usuário (rua, numero, bairro, cidade, estado)
e depois exibe o endereço completo.

Ex. Rua das Algarobas, 113, Centro, Apodi-RN.

'''

rua = input("Nome da rua: ")
numero = input("Número da casa: ")
bairro = input("Nome do Bairro: ")
cidade = input("Nome da Cidade: ")
estado = input("Sigla do Estado: ")

print(f"{rua}, nº {numero}, {bairro}, {cidade} - {estado}.")

