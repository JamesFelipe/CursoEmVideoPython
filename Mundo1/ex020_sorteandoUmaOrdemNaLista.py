# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos
# Faça um programa que leia o nome dos quatros e mostre a ordem sorteada
from random import shuffle
nome1 = input('Nome do primeiro aluno: ')
nome2 = input('Nome do segundo aluno: ')
nome3 = input('Nome do terceiro aluno: ')
nome4 = input('Nome do quarto aluno: ')
alunos = [nome1, nome2, nome3, nome4]
shuffle(alunos)
print(f'A ordem de apresentação será: {alunos}')
