# Um professor que sortear um dos seus quatros alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice
nome1 = input('Nome do primeiro aluno: ')
nome2 = input('Nome do segundo aluno: ')
nome3 = input('Nome do terceiro aluno: ')
nome4 = input('Nome do quarto aluno: ')
alunos = [nome1, nome2, nome3, nome4]
print(f'O aluno escolhido foi o {choice(alunos)}')

