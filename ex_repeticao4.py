'''4) Digite as notas de uma prova para uma
turma com a quantidade de alunos digitado pelo
usuário, e calcule a média da turma.
Dica: use uma variável para acumular a soma de
todas as notas, por último, já fora do laço,
faça a divisão para calcular a média.'''

alunos = int(input("Quantos alunos? "))
soma = 0

atual = 1  # 1.VALOR INICIAL

while atual <= alunos: # 2.TESTE LÓGICO
    nota = int(input(f"Digite a nota do aluno {atual}: "))
    soma += nota
    atual += 1 # 3.INCREMENTO

print("Média da turma:", soma/alunos)
