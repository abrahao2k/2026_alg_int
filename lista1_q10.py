'''10) O cardápio de uma lanchonete é dado abaixo.
Prepare um algoritmo que leia a quantidade de cada
item que você consumiu e calcule a conta final.

Hambúrguer................. R$  8,00  
Cheeseburger............... R$ 12,50  
Fritas..................... R$  9,50  
Refrigerante............... R$  7,00  
Milkshake.................. R$ 21,00
'''
h = int(input("Qtd. Hamburguer: "))
c = int(input("Qtd. Cheeseburguer: "))
f = int(input("Qtd. Batata Frita: "))
r = int(input("Qtd. Refrigerante: "))
m = int(input("Qtd. Milkshake: "))

total = h*8 + c*12.5 + f*9.5 + r*7 + m*21

print("Total da conta: R$", total)



